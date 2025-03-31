from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('products/<int:Product_id>',views.product, name="products"),
    path('old_url',views.old_url_redirect, name="old_url"),
    path('new_url',views.new_url, name="new_url")
]