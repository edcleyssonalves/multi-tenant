from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    #path('products/<int:pk>/update/', ..., name='product_update'),
    #path('products/<int:pk>/delete/', ..., name='product_delete'),
]
