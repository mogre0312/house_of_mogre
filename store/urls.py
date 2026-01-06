from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category_list, name="category_list"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("search/", views.search, name="search"),
    path('cart/', views.cart_detail, name='cart'),
    path('cart/add/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("cart/increase/<int:product_id>/", views.increase_qty, name="increase_qty"),
    path("cart/decrease/<int:product_id>/", views.decrease_qty, name="decrease_qty"),
]
