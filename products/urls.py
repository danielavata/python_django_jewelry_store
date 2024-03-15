from django.urls import path, include

from products import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('cart/<int:pk>/', views.CartDetailView.as_view(), name='cart_detail'),
    path('open-cart/', views.open_cart_view, name='open_cart'),
    path('add-product-to-cart/', views.add_product_to_cart, name='add_product_to_cart'),
    path('contact/', views.ContactRequestCreateView.as_view(), name='contact'),

    path('register/', views.ClientCreateView.as_view(), name='register'),
    path('clients/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),

    path('products/', views.ProductListView.as_view(), name='products'),
]
