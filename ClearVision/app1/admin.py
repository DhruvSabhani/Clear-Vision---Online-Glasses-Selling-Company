from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from app1.models import *

class MyUserAdmin(BaseUserAdmin):
    list_display=('id','username','email','phone_no','gender','birthday','password','joind_date','joind_time')
    search_fields=('email','phone_no')
    readonly_fields=('joind_date','joind_time')
    filter_horizontal=()
    list_filter=('joind_date','joind_time',)
    fieldset=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('username','email','phone_no','gender','birthday','password1','password2','joind_date','joind_time'),
        }),
    )

    ordering=('email',)
admin.site.register(User, MyUserAdmin)  

class GogglesTypesAdmin(admin.ModelAdmin):
    list_display=('id','is_active','goggles_types_id','goggles_types_img','goggles_types_name','goggles_types_informations','joind_date','joind_time')
    search_fields=('is_active','goggles_types_id','goggles_types_img','goggles_types_name','goggles_types_informations','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('is_active','goggles_types_id','goggles_types_img','goggles_types_name','goggles_types_informations','joind_date','joind_time'),
        }),
    )
admin.site.register(Gogglestype, GogglesTypesAdmin)  

class GogglesBrandsAdmin(admin.ModelAdmin):
    list_display=('id','is_active','goggles_brand_id','goggles_brand_img','goggles_brand_name','goggles_brand_informations','joind_date','joind_time')
    search_fields=('is_active','goggles_brand_id','goggles_brand_img','goggles_brand_name','goggles_brand_informations','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('is_active','goggles_brand_id','goggles_brand_img','goggles_brand_name','goggles_brand_informations','joind_date','joind_time'),
        }),
    )
admin.site.register(Gogglesbrand, GogglesBrandsAdmin)  

class GogglesAdmin(admin.ModelAdmin):
    list_display=('id','is_active','goggles_brand_id','goggles_types_id','goggles_id','goggles_font_img','goggles_name','goggles_price','goggles_discount','goggles_informations','goggles_gender','goggles_model_name','goggles_color','goggles_size','goggles_width','goggles_height','goggles_weight','goggles_material','goggles_warranty','goggles_shape','goggles_review','goggles_quantity','goggles_img1','goggles_img2','goggles_img3','goggles_img4','goggles_img5','goggles_img6','goggles_img7','goggles_img8','goggles_img9','goggles_img10','joind_date','joind_time')

    search_fields=('is_active','goggles_brand_id','goggles_types_id','goggles_id','goggles_font_img','goggles_name','goggles_price','goggles_discount','goggles_informations','goggles_gender','goggles_model_name','goggles_color','goggles_size','goggles_width','goggles_height','goggles_weight','goggles_material','goggles_warranty','goggles_shape','goggles_review','goggles_quantity','goggles_img1','goggles_img2','goggles_img3','goggles_img4','goggles_img5','goggles_img6','goggles_img7','goggles_img8','goggles_img9','goggles_img10','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('is_active','goggles_brand_id','goggles_types_id','goggles_id','goggles_font_img','goggles_name','goggles_price','goggles_discount','goggles_informations','goggles_gender','goggles_model_name','goggles_color','goggles_size','goggles_width','goggles_height','goggles_weight','goggles_material','goggles_warranty','goggles_shape','goggles_review','goggles_quantity','goggles_img1','goggles_img2','goggles_img3','goggles_img4','goggles_img5','goggles_img6','goggles_img7','goggles_img8','goggles_img9','goggles_img10','joind_date','joind_time'),
        }),
    )
admin.site.register(Goggles, GogglesAdmin)  

class AddressAdmin(admin.ModelAdmin):
    list_display=('id','userid','is_active','full_name','useremail','house_no','colony_name','city_name','pincode','state','country','joind_date','joind_time')
    search_fields=('userid','is_active','full_name','useremail','house_no','colony_name','city_name','pincode','state','country','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('userid','is_active','full_name','useremail','house_no','colony_name','city_name','pincode','state','country','joind_date','joind_time'),
        }),
    )
admin.site.register(Address, AddressAdmin)  

class CustomerReviewsAdmin(admin.ModelAdmin):
    list_display=('id','goggles_cord','is_active','photos','videos','description','joind_date','joind_time')
    search_fields=('goggles_cord','is_active','photos','videos','description','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('goggles_cord','is_active','photos','videos','description','joind_date','joind_time'),
        }),
    )
admin.site.register(CustomerReviews, CustomerReviewsAdmin)  

class CouponsAdmin(admin.ModelAdmin):
    list_display=('id','coupon_code','is_active','home_screen_is_active','coupon_font_img','coupon_name','goggles_select','categories_select','brands_select','Gender_select','coupon_discount','coupon_informations','coupon_img_1','coupon_img_2','coupon_img_3','coupon_img_4','coupon_img_5','joind_date','joind_time')
    search_fields=('id','coupon_code','is_active','home_screen_is_active','coupon_font_img','coupon_name','goggles_select','categories_select','brands_select','Gender_select','coupon_discount','coupon_informations','coupon_img_1','coupon_img_2','coupon_img_3','coupon_img_4','coupon_img_5','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('id','coupon_code','is_active','home_screen_is_active','coupon_font_img','coupon_name','goggles_select','categories_select','brands_select','Gender_select','coupon_discount','coupon_informations','coupon_img_1','coupon_img_2','coupon_img_3','coupon_img_4','coupon_img_5','joind_date','joind_time'),
        }),
    )
admin.site.register(Coupons, CouponsAdmin)  

class OrdersAdmin(admin.ModelAdmin):
    list_display=('order_id','item_id','item_name','item_image','item_rating','item_quantity','item_delivery_date','item_distance','item_delivery_charges','total_item_amount','item_address_id','item_payments','joind_date','joind_time')
    search_fields=('order_id','item_id','item_name','item_image','item_rating','item_quantity','item_delivery_date','item_distance','item_delivery_charges','total_item_amount','item_address_id','item_payments','joind_date','joind_time')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('order_id','item_id','item_name','item_image','item_rating','item_quantity','item_delivery_date','item_distance','item_delivery_charges','total_item_amount','item_address_id','item_payments','joind_date','joind_time'),
        }),
    )
admin.site.register(Orders, OrdersAdmin)  

class CartItemAdmin(admin.ModelAdmin):
    list_display=('cart_id','user_id','item','item_quantity')
    search_fields=('cart_id','user_id','item','item_quantity')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'classes':('wide'),
            'fields':('cart_id','user_id','item','item_quantity'),
        }),
    )
admin.site.register(CartItem, CartItemAdmin)  

class WishlistTableAdmin(admin.ModelAdmin):
    list_display=('id','user_id','goggles_id')
    search_fields=('id','user_id','goggles_id')
    filter_horizontal=()
    fieldsets=()

    add_fieldsets=(
        (None, {
            'class':('wide'),
            'fields':('id','user_id','goggles_id'),
        }),
    )
admin.site.register(WishlistTable, WishlistTableAdmin)
