from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class UserInformation(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "User's information"

    def __str__(self) -> str:
        return f"{self.nickname} ({self.user!r})"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, default="")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)]
    )
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True, default="")

    class Meta:
        unique_together = ["user", "slug"]

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to=Product, through="ProductInCart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}'s cart"
    
class ProductInCart(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Products in cart"

    def __str__(self) -> str:
        return f"{self.product} ({self.quantity})"

class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ManyToManyField(to='Product', through='ProductInOrder')
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}'s order"


class ProductInOrder(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = "Products in order"

    def __str__(self) -> str:
        return f"{self.product} ({self.quantity})"
    
class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}'s review for {self.product}"

class OwnedProgram(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_acquired = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Owned Programs"

    def __str__(self):
        return f"{self.user}'s owned program: {self.product}"
