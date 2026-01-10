from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from app1.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app1.forms import *
import datetime


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    if request.method == "POST":
        userwarning = WishlistTableForm(request.POST)
        if userwarning.is_valid():
            userwarning.save()
            return redirect("/")
    else:
        userwarning = WishlistTableForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_coupons = Coupons.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()

    total_user_wishlist = WishlistTable.objects.all()

    goggles_eyeglasses = Goggles.objects.filter(goggles_types_id=1).values()
    goggles_eyeglasses_count = Goggles.objects.filter(goggles_types_id=1).count()

    goggles_progressive_lenses = Goggles.objects.filter(goggles_types_id=2).values()
    goggles_progressive_lenses_count = Goggles.objects.filter(
        goggles_types_id=2
    ).count()

    goggles_power_sunglasses = Goggles.objects.filter(goggles_types_id=3).values()
    goggles_power_sunglasses_count = Goggles.objects.filter(goggles_types_id=3).count()

    goggles_screen_glasses = Goggles.objects.filter(goggles_types_id=4).values()
    goggles_screen_glasses_count = Goggles.objects.filter(goggles_types_id=4).count()

    goggles_sunglasses = Goggles.objects.filter(goggles_types_id=5).values()
    goggles_sunglasses_count = Goggles.objects.filter(goggles_types_id=5).count()

    goggles_safety_glasses = Goggles.objects.filter(goggles_types_id=6).values()
    goggles_safety_glasses_count = Goggles.objects.filter(goggles_types_id=6).count()

    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()

    now = datetime.datetime.now()
    # goggles_all = Goggles.objects.select_related('goggles_brand_id','goggles_types_id').all()
    context = {
        "af": af,
        "userwarning": userwarning,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_coupons": goggles_coupons,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "total_user_wishlist": total_user_wishlist,
        "goggles_type_value": goggles_type_value,
        "goggles_eyeglasses": goggles_eyeglasses,
        "goggles_eyeglasses_count": goggles_eyeglasses_count,
        "goggles_progressive_lenses": goggles_progressive_lenses,
        "goggles_progressive_lenses_count": goggles_progressive_lenses_count,
        "goggles_power_sunglasses": goggles_power_sunglasses,
        "goggles_power_sunglasses_count": goggles_power_sunglasses_count,
        "goggles_screen_glasses": goggles_screen_glasses,
        "goggles_screen_glasses_count": goggles_screen_glasses_count,
        "goggles_sunglasses": goggles_sunglasses,
        "goggles_sunglasses_count": goggles_sunglasses_count,
        "goggles_safety_glasses": goggles_safety_glasses,
        "goggles_safety_glasses_count": goggles_safety_glasses_count,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
        # 'goggles_all':goggles_all
    }
    return render(request, "Index.html", context)


def Goggles_show(request, goggles_types_name, goggles_types_id):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    name = goggles_types_name
    id = goggles_types_id
    address = Address.objects.all()
    now = datetime.datetime.now()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_name = Gogglestype.objects.filter(goggles_types_name=name).values()
    goggles_show = Goggles.objects.filter(goggles_types_id=id).values()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    context = {
        "af": af,
        "address": address,
        "datetime": now,
        "goggles_brand": goggles_brand,
        "goggless": goggless,
        "goggles_type_name": goggles_type_name,
        "goggles_show": goggles_show,
        "goggles_type": goggles_type,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
    }
    return render(request, "goggles_show.html", context)


def Goggles_Cart(
    request, goggles_types_name, goggles_types_id, goggles_brand_id, goggles_id
):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    gogglestypesname = goggles_types_name
    gogglestypeid = goggles_types_id
    gogglesbrandid = goggles_brand_id
    goggleid = goggles_id
    address = Address.objects.all()
    now = datetime.datetime.now()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    g_id = Goggles.objects.filter(
        goggles_types_id=gogglestypeid, goggles_id=goggleid
    ).values()
    g_type = Gogglestype.objects.filter(goggles_types_id=gogglestypeid).values()
    g_brand = Gogglesbrand.objects.filter(goggles_brand_id=gogglesbrandid).values()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    context = {
        "af": af,
        "address": address,
        "datetime": now,
        "goggles_brand": goggles_brand,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "gogglestypesname": gogglestypesname,
        "g_type": g_type,
        "g_brand": g_brand,
        "g_id": g_id,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
    }
    return render(request, "cart.html", context)


def Cartview(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    if request.method == "POST":
        itemid = request.POST["itemid"]
        quantity = request.POST["1To9Quantity"]

        cart = CartItem.objects.update(item_id=itemid, item_quantity=quantity)

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_customer_reviews = CustomerReviews.objects.all()
    goggles_coupons = Coupons.objects.all()
    goggles_cart_item = CartItem.objects.all()
    goggles_wishlist_table = WishlistTable.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    goggles_cart_item_filter = CartItem.objects.filter(user_id=request.user.id)
    goggles_cart_item_filter_values = CartItem.objects.filter(
        user_id=request.user.id
    ).values()
    goggles_cart_item_filter_count = CartItem.objects.filter(
        user_id=request.user.id
    ).count()
    total = sum(item.subtotal() for item in goggles_cart_item_filter)
    totaldiscount = sum(item.subdiscount() for item in goggles_cart_item_filter)
    ta = sum(item.totalamount() for item in goggles_cart_item_filter)
    now = datetime.datetime.now()

    context = {
        "af": af,
        "address": address,
        "Goggles": Goggles,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_customer_reviews": goggles_customer_reviews,
        "goggles_coupons": goggles_coupons,
        "goggles_cart_item": goggles_cart_item,
        "goggles_wishlist_table": goggles_wishlist_table,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "goggles_cart_item_filter": goggles_cart_item_filter,
        "goggles_cart_item_filter_values": goggles_cart_item_filter_values,
        "total": total,
        "totaldiscount": totaldiscount,
        "ta": ta,
        "goggles_cart_item_filter_count": goggles_cart_item_filter_count,
        "datetime": now,
    }
    return render(request, "cart_view.html", context)


def CartviewRemove(request, item_id):
    cart_item_remove = CartItem.objects.filter(item_id=item_id)
    cart_item_remove.delete()
    messages.success(request, "Item is Remove Successfully")
    return redirect("/cart-view/")


def Goggles_men(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()

    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "goggles_show.html", context)


def Orders(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()
    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "orders.html", context)


def Brands(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_all = Goggles.objects.filter(goggles_gender="All").values()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()
    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_all": goggles_all,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "brands.html", context)


def AddToCart(request, goggles_id):
    if request.user.is_authenticated:
        u_id = request.user.id
        i_id = goggles_id
        user_and_item_check = CartItem.objects.filter(user_id=u_id, item_id=i_id)
        if user_and_item_check.exists():
            messages.warning(request, "Item is already Add To Cart")
            return redirect("/")
        else:
            add = CartItem.objects.create(user_id=u_id, item_id=i_id, item_quantity=1)
            add.save()
            messages.success(request, "Item is Add to Cart Successfully")
            return redirect("/cart-view/")

    address = Address.objects.all()
    context = {"address": address}
    return render(request, "cart_view.html", context)


def Wishlist(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()
    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "wishlist.html", context)


def Ordershow(request):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()
    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "order_show.html", context)


def Login(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email_login = request.POST["email_login"]
        password_login = request.POST["password_login"]

        email_check = User.objects.filter(email=email_login)

        if not email_check.exists():
            messages.warning(request, "Please Valid Email ID Enter...")
            return HttpResponseRedirect(request.path_info)

        user = authenticate(email=email_login, password=password_login)
        if user:
            login(request, user)
            messages.success(request, "Successfully Login...")
            return redirect("/")
        messages.warning(request, "Invalid Email ID and Password")
        return HttpResponseRedirect(request.path_info)

    return render(request, "User_Login.html")


def Register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        name_register = request.POST["name_register"]
        phone_register = request.POST["phone_register"]
        gender_register = request.POST["gender_register"]
        birthday_register = request.POST["birthday_register"]
        email_register = request.POST["email_register"]
        password_register = request.POST["password_register"]
        confirm_password_register = request.POST["confirm_password_register"]
        joind_date = request.POST["joind_date"]
        joind_time = request.POST["joind_time"]

        email_check = User.objects.filter(email=email_register)
        phone_check = User.objects.filter(phone_no=phone_register)

        if name_register == "":
            messages.warning(request, "Please enter the username")
            return HttpResponseRedirect(request.path_info)
        elif phone_register == "":
            messages.warning(request, "Please enter the phone no.")
            return HttpResponseRedirect(request.path_info)
        elif email_register == "":
            messages.warning(request, "Please enter the email")
            return HttpResponseRedirect(request.path_info)
        elif password_register == "":
            messages.warning(request, "Please enter the password")
            return HttpResponseRedirect(request.path_info)
        elif confirm_password_register == "":
            messages.warning(request, "Please enter the confirm password")
            return HttpResponseRedirect(request.path_info)
        elif email_check.exists():
            messages.warning(request, "Your Email Already Exists")
            return HttpResponseRedirect(request.path_info)
        elif phone_check.exists():
            messages.warning(request, "Your Phone Number Already Exists")
            return HttpResponseRedirect(request.path_info)
        elif len(phone_register) != 10:
            messages.warning(request, "Number Should Be 10 Digit...")
            return HttpResponseRedirect(request.path_info)
        elif password_register != confirm_password_register:
            messages.warning(request, "Password and Confirm Password Did Not Match...")
            return HttpResponseRedirect(request.path_info)
        else:
            user = User.objects.create(
                username=name_register,
                email=email_register,
                phone_no=phone_register,
                gender=gender_register,
                birthday=birthday_register,
                joind_date=joind_date,
                joind_time=joind_time,
            )
            user.set_password(password_register)
            user.save()

            messages.success(request, "Register Successfully...")
            return redirect("/login/")

    now = datetime.datetime.now()

    return render(request, "User_Register.html", {"datetime": now})


def Logout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("/login/")


def Profile(request, id):
    if request.method == "POST":
        af = AddressForm(request.POST)
        if af.is_valid():
            af.save()
            messages.success(request, "Add New Address Successfully...")
            return redirect("/")
    else:
        af = AddressForm()

    try:
        u_id = int(request.GET["user_id"])
        a_id = int(request.GET["address_select"])
        Address.objects.filter(userid=u_id).update(is_active=False)
        Address.objects.filter(id=a_id).update(is_active=True)
    except:
        pass

    if request.method == "POST":
        name_register = request.POST["name_register"]
        email_register = request.POST["email_register"]
        phone_register = request.POST["phone_register"]
        gender_register = request.POST["gender_register"]
        birthday_register = request.POST["birthday_register"]

        if len(phone_register) != 10:
            messages.warning(request, "Number Should Be 10 Digit...")
            return HttpResponseRedirect(request.path_info)
        else:
            user = User.objects.update(
                username=name_register,
                email=email_register,
                phone_no=phone_register,
                gender=gender_register,
                birthday=birthday_register,
            )
            # user.save()
            messages.success(request, "Update Successfully...")

    address = Address.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_type_value = (
        Gogglestype.objects.all().order_by("-goggles_types_name").values()
    )
    goggles_count = Goggles.objects.all().count()
    goggles_men = Goggles.objects.filter(goggles_gender="Men").values()
    goggles_women = Goggles.objects.filter(goggles_gender="Women").values()
    goggles_kids = Goggles.objects.filter(goggles_gender="Kids").values()
    now = datetime.datetime.now()
    context = {
        "af": af,
        "address": address,
        "goggles_brand": goggles_brand,
        "goggles_type": goggles_type,
        "goggles_type_count": goggles_type_count,
        "goggless": goggless,
        "goggles_count": goggles_count,
        "goggles_type_value": goggles_type_value,
        "goggles_men": goggles_men,
        "goggles_women": goggles_women,
        "goggles_kids": goggles_kids,
        "datetime": now,
    }
    return render(request, "User_Profile.html", context)


def Delete_Profile(request, id):
    try:
        u = User.objects.filter(id=id)
        u.delete()
        messages.success(request, "Delete User Profile Successfully")
    except:
        messages.error(request, "The user not found")
    return redirect("/")
