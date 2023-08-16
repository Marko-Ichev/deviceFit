from django.contrib import admin
from . import models
from django.http.request import HttpRequest


class UserInformationAdmin(admin.ModelAdmin[models.UserInformation]):
    list_display = ["nickname", "user"]
    search_fields = ["nickname", "user__username", "user__email"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, obj: models.UserInformation | None = None
    ) -> bool:
        return (
            (obj is not None and obj.user == request.user)
            or request.user.is_staff
            or request.user.is_superuser
        )

    def has_delete_permission(
        self, request: HttpRequest, obj: models.UserInformation | None = None
    ) -> bool:
        return self.has_change_permission(request, obj)

    def has_view_permission(
        self, request: HttpRequest, _: models.UserInformation | None = None
    ) -> bool:
        return request.user.is_authenticated


class CategoryAdmin(admin.ModelAdmin[models.Category]):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ["name", "slug"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.Category | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.Category | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.Category | None = None
    ) -> bool:
        return request.user.is_authenticated


class ProductAdmin(admin.ModelAdmin[models.Product]):
    list_display = ["name", "price"]
    prepopulated_fields = {"slug": ["name"]}
    list_filter = ["category", "user"]
    search_fields = ["name", "description", "category__name", "user__username"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.Product | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.Product | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.Product | None = None
    ) -> bool:
        return request.user.is_authenticated


class CartAdmin(admin.ModelAdmin[models.Cart]):
    list_display = ["user"]
    search_fields = ["user__username"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.Cart | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.Cart | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.Cart | None = None
    ) -> bool:
        return request.user.is_authenticated


class ProductInCartAdmin(admin.ModelAdmin[models.ProductInCart]):
    list_display = ["cart", "product", "quantity"]
    search_fields = ["cart__user__username", "product__name"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.ProductInCart | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.ProductInCart | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.ProductInCart | None = None
    ) -> bool:
        return request.user.is_authenticated


class OrderAdmin(admin.ModelAdmin[models.Order]):
    list_display = ["user"]
    search_fields = ["user__username", "products__name"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.Order | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.Order | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.Order | None = None
    ) -> bool:
        return request.user.is_authenticated


class ProductInOrderAdmin(admin.ModelAdmin[models.ProductInOrder]):
    list_display = ["order", "product", "quantity"]
    search_fields = ["order__user__username", "product__name"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.ProductInOrder | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.ProductInOrder | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.ProductInOrder | None = None
    ) -> bool:
        return request.user.is_authenticated
    

class ReviewAdmin(admin.ModelAdmin[models.Review]):
    list_display = ["user", "product", "rating"]
    list_filter = ["user", "product", "rating"]
    search_fields = ["user__username", "product__name", "product__description"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, _: models.Review | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(
        self, request: HttpRequest, _: models.Review | None = None
    ) -> bool:
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(
        self, request: HttpRequest, _: models.Review | None = None
    ) -> bool:
        return request.user.is_authenticated
    
class OwnedProgramAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "order", "date_acquired"]
    list_filter = ["user", "product", "order"]
    search_fields = ["user__username", "product__name", "order__user__username"]

    def has_add_permission(self, request):
        return request.user.is_staff or request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_authenticated


admin.site.register(models.UserInformation, UserInformationAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.ProductInCart, ProductInCartAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.ProductInOrder, ProductInOrderAdmin)
admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.OwnedProgram, OwnedProgramAdmin)
