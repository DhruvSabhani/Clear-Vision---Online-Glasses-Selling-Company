from django.contrib import admin
from django.urls import path
from adminApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/',views.Dashboard, name="Dashboard"),

    path('dashboard/orders/',views.OrdersAdmin, name="Orders"),

    path('categories/',views.Categories, name="Categories"),
    path('categories/delete/<int:goggles_types_id>/',views.CategoriesDelete, name="Categories Delete"),
    path('categories/edit/<int:goggles_types_id>/',views.CategoriesEdit, name="Categories Edit"),
    path('categories/goggles/view-<int:goggles_types_id>/',views.CategoriesGogglesView, name="Goggles View"),

    path('add-product/',views.Add_product, name="Add Product"),
    path('goggle/view-<int:goggles_id>/',views.GoogleView, name="Goggles View"),
    path('goggle/edit-<int:goggles_id>/',views.GoogleEdit, name="Goggles Edit"),
    path('goggle/delete-<int:goggles_id>/',views.GoogleDelete, name="Goggles Delete"),

    path('goggle/delete/image1-<str:goggles_img1>/',views.Img1, name="Goggles Image 1 Delete"),
    path('goggle/delete/image2-<str:goggles_img2>/',views.Img2, name="Goggles Image 2 Delete"),
    path('goggle/delete/image3-<str:goggles_img3>/',views.Img3, name="Goggles Image 3 Delete"),
    path('goggle/delete/image4-<str:goggles_img4>/',views.Img4, name="Goggles Image 4 Delete"),
    path('goggle/delete/image5-<str:goggles_img5>/',views.Img5, name="Goggles Image 5 Delete"),
    path('goggle/delete/image6-<str:goggles_img6>/',views.Img6, name="Goggles Image 6 Delete"),
    path('goggle/delete/image7-<str:goggles_img7>/',views.Img7, name="Goggles Image 7 Delete"),
    path('goggle/delete/image8-<str:goggles_img8>/',views.Img8, name="Goggles Image 8 Delete"),
    path('goggle/delete/image9-<str:goggles_img9>/',views.Img9, name="Goggles Image 9 Delete"),
    path('goggle/delete/image10-<str:goggles_img10>/',views.Img10, name="Goggles Image 10 Delete"),

    path('dashboard/brands/',views.Brands, name="Brands"),
    path('brands/view-<int:goggles_brand_id>/',views.BrandView, name="Brand View"),
    path('brands/edit-<int:goggles_brand_id>/',views.BrandEdit, name="Brand Edit"),
    path('brands/delete-<int:goggles_brand_id>/',views.BrandDelete, name="Brand Delete"),

    path('coupons/',views.Coupons_modal, name="Coupons"),
    path('coupons/view-<int:coupon_code>/',views.CouponsView, name="Coupons View"),
    path('coupons/edit-<str:coupon_code>/',views.CouponsEdit, name="Coupons Edit"),
    path('coupons/delete-<int:coupon_code>/',views.CouponsDelete, name="Coupons Delete"),

    path('users/',views.Users, name="Users"),
    path('users/view-<int:id>/',views.UserView, name="User View"),

    path('reviews/',views.Reviews, name="Reviews"),

    path('dashboard-login/',views.Login_Admin, name="Login Admin"),

    path('admin-logout/',views.Admin_Logout, name="Logout"),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)