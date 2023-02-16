from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='ecommerce-home'), #name should be specific
    path('about/', views.about, name='ecommerce-about'),
    path('cart_list/', views.cart_list, name='cart_list'),
    path('cart_list/add/', views.cart_add, name='cart_add'),
    path('cart_list/<int:pk>/update/', views.cart_update, name='cart_update'),
    path('cart_list/<int:pk>/delete/', views.cart_delete, name='cart_delete'),


    path('productdetails/', views.productdetails, name='ecommerce-productdetails'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
