from django.forms import ModelForm, NumberInput, TextInput, Textarea, FileInput
from adminApp.models import *
from app1.models import *

class TypesForm(ModelForm):
    class Meta:
        model = Gogglestype
        fields = ['goggles_types_id','is_active','goggles_types_img','goggles_types_name','goggles_types_informations','joind_date','joind_time']
        widgets = {
            'goggles_types_id' : NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles category id',
                'required': ''
            }),
            'goggles_types_img' : FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_types_name' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles category name',
                'required': ''
            }),
            'goggles_types_informations' : Textarea(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles category information',
                'rows' : '5',
                'required': ''
            })
        }

class GogglesForm(ModelForm):
    class Meta:
        model = Goggles
        fields = ['is_active','goggles_brand_id','goggles_types_id','goggles_id','goggles_font_img','goggles_name','goggles_price','goggles_discount','goggles_informations','goggles_gender','goggles_model_name','goggles_color','goggles_size','goggles_width','goggles_height','goggles_weight','goggles_material','goggles_warranty','goggles_shape','goggles_review','goggles_quantity','goggles_img1','goggles_img2','goggles_img3','goggles_img4','goggles_img5','goggles_img6','goggles_img7','goggles_img8','goggles_img9','goggles_img10','joind_date','joind_time']
        widgets = {
            'goggles_id': NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles id',
                'required': ''
            }),
            'goggles_name': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles name',
                'required': ''
            }),
            'goggles_font_img': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_price': NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles price',
                'required': ''
            }),
            'goggles_discount': NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles discount'
            }),
            'goggles_model_name': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles model name'
            }),
            'goggles_color': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles color'
            }),
            'goggles_size': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles size'
            }),
            'goggles_width': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles width'
            }),
            'goggles_height': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles height'
            }),
            'goggles_weight': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles weight'
            }),
            'goggles_material': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles material'
            }),
            'goggles_warranty': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles warranty'
            }),
            'goggles_shape': TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles shape'
            }),
            'goggles_quantity': NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles quantity'
            }),
            'goggles_img1': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img2': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img3': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img4': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img5': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img6': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img7': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img8': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img9': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_img10': FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_informations' : Textarea(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles information',
                'rows' : '5'
            })
        }

class BrandsForm(ModelForm):
    class Meta:
        model = Gogglesbrand
        fields = ['goggles_brand_id','is_active','goggles_brand_img','goggles_brand_name','goggles_brand_informations','joind_date','joind_time']
        widgets = {
            'goggles_brand_id' : NumberInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles brand id',
                'required': ''
            }),
            'goggles_brand_img' : FileInput(attrs={
                'accept':"image/*",
                'style': 'font-size: 17px !important;',
                'class': "form-control"
            }),
            'goggles_brand_name' : TextInput(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles brand name',
                'required': ''
            }),
            'goggles_brand_informations' : Textarea(attrs={
                'class': "form-control",
                'style': 'font-size: 17px !important;',
                'placeholder': 'Enter your goggles brand information',
                'rows' : '5',
                'required': ''
            })
        }

class CouponsForm(ModelForm):
    class Meta:
        model = Coupons
        fields = ['coupon_code','is_active','home_screen_is_active','coupon_font_img','coupon_name','goggles_select','categories_select','brands_select','Gender_select','coupon_discount','coupon_informations','coupon_img_1','coupon_img_2','coupon_img_3','coupon_img_4','coupon_img_5','joind_date','joind_time']
        widgets = {
            "coupon_code": TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your coupon code",
                'required': ''
            }),
            "coupon_font_img": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
            "coupon_name": TextInput(attrs={
                "class":"form-control",
                "placeholder": "Enter your coupon name",
                "required": ""
            }),
            "coupon_discount": NumberInput(attrs={
                "class":"form-control",
                "placeholder": "Enter your coupon price discount",
                "required": ""
            }),
            "coupon_informations": Textarea(attrs={
                "class":"form-control",
                "placeholder": "Enter your coupon information",
                "rows":"2"
            }),
            "coupon_img_1": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
            "coupon_img_2": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
            "coupon_img_3": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
            "coupon_img_4": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
            "coupon_img_5": FileInput(attrs={
                'accept':"image/*",
                "class":"form-control"
            }),
        }        