"""
URL configuration for deviceFit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", admin.site.login, name="login"),
    path("logout/", admin.site.logout, name="logout"),
    path("products/", views.products, name="products"),
    path("category/<str:slug>/", views.category, name="category"),
    path("cart/", views.cart, name="cart"),
    path("admin/", admin.site.urls, name="admin"),
    path("profile/", views.profile, name="profile"),
    path("add_to_cart/<str:slug>/", views.add_to_cart, name="add_to_cart"),
    path(
        "remove_from_cart/<str:slug>/", views.remove_from_cart, name="remove_from_cart"
    ),
    path("checkout/", views.checkout, name="checkout"),
    path("empty_cart/", views.empty_cart, name="empty_cart"),
    path("product/<str:slug>", views.product, name="product"),
    path("post_review/<str:slug>", views.post_review, name="post_review"),
    path("owned_programs/", views.owned_programs, name="owned_programs"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]