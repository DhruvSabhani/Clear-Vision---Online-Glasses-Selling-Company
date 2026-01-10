from django.db import models
from django.contrib.auth.models import AbstractUser
from app1.manager import UserManager

STATE_CHOICE = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
)

COUNTRY_CHOICE = (("India", "India"),)

GENDER_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

GOGGLES_GENDER = (
    ("All", "All"),
    ("Men", "Men"),
    ("Women", "Women"),
    ("Kids", "Kids"),
)


class User(AbstractUser):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    email = models.EmailField(verbose_name="Email Address", max_length=20, unique=True)
    phone_no = models.CharField(max_length=10, blank=True, verbose_name="Phone No")
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=6, blank=True, verbose_name="Gender"
    )
    birthday = models.CharField(max_length=10, blank=True, verbose_name="Birthday")
    joind_date = models.CharField(max_length=10, blank=True, verbose_name="Joind Date")
    joind_time = models.CharField(max_length=10, blank=True, verbose_name="Joind Time")

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["gender", "birthday"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lebel):
        return True


class Gogglestype(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    is_active = models.CharField(max_length=5, verbose_name="Is Active", blank=True)
    goggles_types_id = models.CharField(
        max_length=10, blank=True, verbose_name="Goggles Types ID"
    )
    goggles_types_img = models.ImageField(
        upload_to="", blank=True, verbose_name="Goggles Types Images"
    )
    goggles_types_name = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Types Name"
    )
    goggles_types_informations = models.CharField(
        max_length=10000, blank=True, verbose_name="Goggles Types Informations"
    )
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.goggles_types_id


class Gogglesbrand(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    is_active = models.CharField(max_length=5, verbose_name="Is Active", blank=True)
    goggles_brand_id = models.CharField(
        max_length=10, blank=True, verbose_name="Goggles Brand ID"
    )
    goggles_brand_img = models.ImageField(
        upload_to="", blank=True, verbose_name="Goggles Brand Images"
    )
    goggles_brand_name = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Brand Name"
    )
    goggles_brand_informations = models.CharField(
        max_length=1000, blank=True, verbose_name="Goggles Brand Informations"
    )
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.goggles_brand_id


class Goggles(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    is_active = models.CharField(max_length=5, verbose_name="Is Active", blank=True)
    goggles_brand_id = models.CharField(
        max_length=10, blank=True, verbose_name="Brand ID"
    )
    goggles_types_id = models.CharField(
        max_length=10, blank=True, verbose_name="Type ID"
    )
    goggles_id = models.IntegerField()
    goggles_font_img = models.ImageField(
        upload_to="", blank=True, verbose_name="Goggles Images"
    )
    goggles_name = models.CharField(
        max_length=50, blank=True, verbose_name="Goggles Name"
    )
    goggles_price = models.IntegerField(blank=True, verbose_name="Goggles Price")
    goggles_discount = models.IntegerField(blank=True, verbose_name="Goggles Discount")
    goggles_informations = models.CharField(
        max_length=1000, blank=True, verbose_name="Goggles Informations"
    )
    goggles_gender = models.CharField(
        choices=GOGGLES_GENDER, max_length=5, blank=True, verbose_name="Goggles Gender"
    )
    goggles_model_name = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Model Name"
    )
    goggles_color = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Color"
    )
    goggles_size = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Size"
    )
    goggles_width = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Width"
    )
    goggles_height = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Height"
    )
    goggles_weight = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Weight"
    )
    goggles_material = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Material"
    )
    goggles_warranty = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Warranty"
    )
    goggles_shape = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Shape"
    )
    goggles_review = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Review"
    )
    goggles_quantity = models.CharField(
        max_length=25, blank=True, verbose_name="Goggles Quantity"
    )
    goggles_img1 = models.ImageField(upload_to="", blank=True, verbose_name="Image 1")
    goggles_img2 = models.ImageField(upload_to="", blank=True, verbose_name="Image 2")
    goggles_img3 = models.ImageField(upload_to="", blank=True, verbose_name="Image 3")
    goggles_img4 = models.ImageField(upload_to="", blank=True, verbose_name="Image 4")
    goggles_img5 = models.ImageField(upload_to="", blank=True, verbose_name="Image 5")
    goggles_img6 = models.ImageField(upload_to="", blank=True, verbose_name="Image 6")
    goggles_img7 = models.ImageField(upload_to="", blank=True, verbose_name="Image 7")
    goggles_img8 = models.ImageField(upload_to="", blank=True, verbose_name="Image 8")
    goggles_img9 = models.ImageField(upload_to="", blank=True, verbose_name="Image 9")
    goggles_img10 = models.ImageField(upload_to="", blank=True, verbose_name="Image 10")
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def discounted_price(self):
        return self.goggles_price * self.goggles_discount / 100

    def __str__(self):
        return self.goggles_name


class Address(models.Model):
    userid = models.CharField(max_length=10, blank=True, verbose_name="User ID")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    full_name = models.CharField(max_length=255, verbose_name="Full Name", blank=True)
    useremail = models.EmailField(verbose_name="Email Address", blank=True)
    house_no = models.CharField(max_length=255, blank=True, verbose_name="House No")
    colony_name = models.CharField(
        max_length=255, blank=True, verbose_name="Colony Name"
    )
    city_name = models.CharField(max_length=255, blank=True, verbose_name="City Name")
    pincode = models.CharField(max_length=255, blank=True, verbose_name="Pincode")
    state = models.CharField(
        choices=STATE_CHOICE, max_length=255, blank=True, verbose_name="State"
    )
    country = models.CharField(
        choices=COUNTRY_CHOICE, max_length=255, blank=True, verbose_name="Country"
    )
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.userid


class CustomerReviews(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    goggles_cord = models.CharField(
        max_length=10, blank=True, verbose_name="Goggles ID"
    )
    is_active = models.CharField(max_length=5, verbose_name="Is Active", blank=True)
    photos = models.ImageField(upload_to="", blank=True, verbose_name="Photos")
    videos = models.FileField(upload_to="", blank=True, verbose_name="Videos")
    description = models.CharField(
        max_length=1000, blank=True, verbose_name="Description"
    )
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.goggles_cord


class Coupons(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    coupon_code = models.CharField(
        max_length=10, unique=True, blank=True, verbose_name="Coupon Code"
    )
    is_active = models.CharField(max_length=5, verbose_name="Is Active", blank=True)
    home_screen_is_active = models.CharField(
        max_length=5, verbose_name="Home Screen is active", blank=True
    )
    coupon_font_img = models.ImageField(
        upload_to="", blank=True, verbose_name="Font Image"
    )
    coupon_name = models.CharField(
        max_length=10, verbose_name="Coupons Name", blank=True
    )
    goggles_select = models.CharField(max_length=25, blank=True, verbose_name="Goggles")
    categories_select = models.CharField(
        max_length=25, blank=True, verbose_name="Categories"
    )
    brands_select = models.CharField(max_length=25, blank=True, verbose_name="Brands")
    Gender_select = models.CharField(max_length=5, blank=True, verbose_name="Gender")
    coupon_discount = models.IntegerField(blank=True, verbose_name="Coupon Discount")
    coupon_informations = models.CharField(
        max_length=1000, blank=True, verbose_name="Coupon Informations"
    )
    coupon_img_1 = models.ImageField(
        upload_to="", blank=True, verbose_name="Coupon Image 1"
    )
    coupon_img_2 = models.ImageField(
        upload_to="", blank=True, verbose_name="Coupon Image 2"
    )
    coupon_img_3 = models.ImageField(
        upload_to="", blank=True, verbose_name="Coupon Image 3"
    )
    coupon_img_4 = models.ImageField(
        upload_to="", blank=True, verbose_name="Coupon Image 4"
    )
    coupon_img_5 = models.ImageField(
        upload_to="", blank=True, verbose_name="Coupon Image 5"
    )
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.coupon_code


class CartItem(models.Model):
    cart_id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="Cart ID"
    )
    user_id = models.IntegerField(blank=True)
    item = models.ForeignKey(Goggles, on_delete=models.CASCADE)
    item_quantity = models.PositiveIntegerField(blank=True, default=1)

    def subtotal(self):
        return self.item_quantity * self.item.goggles_price

    def subdiscount(self):
        return self.item_quantity * self.item.discounted_price()

    def totalamount(self):
        return self.subtotal() - self.subdiscount()

    def __str__(self):
        return f"{self.item.goggles_name} - {self.item_quantity}"


class Orders(models.Model):
    order_id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="Order ID"
    )
    item_id = models.CharField(max_length=10, blank=True, verbose_name="Goggles Cord")
    item_name = models.CharField(
        max_length=100, blank=True, verbose_name="Goggles Name"
    )
    item_image = models.ImageField(
        upload_to="", blank=True, verbose_name="Goggles Image"
    )
    item_rating = models.IntegerField(verbose_name="Item Rating", blank=True)
    item_quantity = models.IntegerField(verbose_name="Item Quantity", blank=True)
    item_delivery_date = models.DateField(blank=True)
    item_distance = models.CharField(
        max_length=5, verbose_name="Item Distance", blank=True
    )
    item_delivery_charges = models.CharField(
        max_length=10, verbose_name="Item Delivery Charges", blank=True
    )
    total_item_amount = models.IntegerField(
        verbose_name="Total Item Amount", blank=True
    )
    item_address_id = models.CharField(
        max_length=10, blank=True, verbose_name="Address ID"
    )
    item_payments = models.IntegerField(verbose_name="Item Payments", blank=True)
    joind_date = models.DateField()
    joind_time = models.TimeField()

    def __str__(self):
        return self.item_id


class WishlistTable(models.Model):
    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    user_id = models.CharField(max_length=10, verbose_name="User ID", blank=True)
    goggles_id = models.CharField(max_length=10, verbose_name="Goggles ID", blank=True)

    def __str__(self):
        return self.user_id
