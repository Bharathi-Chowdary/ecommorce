from django.urls import path
from . import views
urlpatterns = [
    path('', views.store,  name = 'store'),
    
    path('category/<str:category_urls>/', views.store, name='products_by_category'),
    path('category/<str:category_urls>/<str:product_url>/', views.product_detail, name='product_detail'),

]