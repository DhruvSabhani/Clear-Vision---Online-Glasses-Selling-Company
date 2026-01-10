from django.contrib import admin
from django.urls import path
from app1 import views
from app1.views import Register,Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Index, name="Home"),

    path('Men/',views.Goggles_men, name="Goggles Men"),
    
    path('<str:goggles_types_name>-<int:goggles_types_id>',views.Goggles_show, name="Goggles"),
    
    path('<str:goggles_types_name>-<int:goggles_types_id><int:goggles_brand_id>/cart-<int:goggles_id>', views.Goggles_Cart, name="Cart"),
    
    path('add-to-cart/<int:goggles_id>',views.AddToCart, name="Add to Cart"),
    path('orders/',views.Orders, name="Orders"),
    path('order-show/',views.Ordershow, name="Order Show"),

    path('brands/',views.Brands, name="Brands"),
    
    path('cart-view/',views.Cartview, name="Cart View"),
    path('cart_view/remove/<int:item_id>/',views.CartviewRemove, name="Cart Remove"),

    path('login/',views.Login, name="Login"),
    
    path('signup/',views.Register, name="Register"),
    
    path('profile/<int:id>',views.Profile, name="Profile"),
    
    path('logout/',views.Logout, name="Logout"),
    
    path('delete_profile/<int:id>',views.Delete_Profile, name="Delete_Profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
