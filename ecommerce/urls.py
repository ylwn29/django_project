from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='ecommerce-home'), #name should be specific
    path('about/', views.about, name='ecommerce-about'),
    path('shoppingcart/', views.shoppingcart, name='ecommerce-shoppingcart'),
    path('productdetails/', views.productdetails, name='ecommerce-productdetails'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
