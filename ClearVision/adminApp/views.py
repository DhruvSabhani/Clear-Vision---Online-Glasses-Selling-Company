from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from adminApp.models import UserAdmin
from app1.models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from adminApp.forms import *
import datetime

# Create your views here.


def Login_Admin(request):
    if request.method == "POST":
        email_login = request.POST.get("email_admin")
        password_login = request.POST.get("password_admin")

        email_check = UserAdmin.objects.filter(email=email_login)
        password_check = UserAdmin.objects.filter(password=password_login)

        if email_login == "":
            messages.warning(request, "Enter your email")
            return HttpResponseRedirect(request.path_info)

        if not email_check.exists():
            messages.warning(request, "Please Valid Email ID Enter...")
            return HttpResponseRedirect(request.path_info)

        elif password_login == "":
            messages.warning(request, "Enter your password")
            return HttpResponseRedirect(request.path_info)

        elif len(password_login) <= 3:
            messages.warning(request, "Enter your password 4 or more digit")
            return HttpResponseRedirect(request.path_info)

        elif not password_check.exists():
            messages.warning(request, "Please Valid Password Enter...")
            return HttpResponseRedirect(request.path_info)
        else:
            request.session["email"] = request.POST.get("email_admin")
            messages.success(request, "Successfully Login...")
            return redirect("/dashboard/")

    return render(request, "admin_login.html")


def Dashboard(request):
    if request.session.has_key("email"):
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()
        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()

        email = UserAdmin.objects.filter(email=request.session["email"]).values()

        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
        }
        return render(request, "admin.html", context)
    else:
        return redirect("/dashboard-login/")


def OrdersAdmin(request):
    if request.session.has_key("email"):
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()

        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()

        email = UserAdmin.objects.filter(email=request.session["email"]).values()

        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
        }
        return render(request, "admin_orders.html", context)
    else:
        return redirect("/dashboard-login/")


def Categories(request):
    if request.session.has_key("email"):
        if request.method == "POST":
            form = TypesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "ADD Goggles Category Successfully...")
                return redirect("/categories/")
        else:
            form = TypesForm()

        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()

        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()

        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        now = datetime.datetime.now()

        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
            "datetime": now,
            "form": form,
        }
        return render(request, "admin_categories.html", context)
    else:
        return redirect("/dashboard-login/")


def CategoriesDelete(request, goggles_types_id):
    try:
        cetegories_delete = Gogglestype.objects.filter(
            goggles_types_id=goggles_types_id
        )
        cetegories_delete.delete()
        messages.success(request, "Delete Categories Successfully")
        return redirect("/categories/")
    except:
        messages.error(request, "The user not found")
        return redirect("/categories/")

    return render(request, "admin_categories.html")


def CategoriesEdit(request, goggles_types_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    cetegories_edit = Gogglestype.objects.filter(
        goggles_types_id=goggles_types_id
    ).values()
    now = datetime.datetime.now()
    cetegoriesedit = Gogglestype.objects.get(goggles_types_id=goggles_types_id)

    form = TypesForm(request.POST, request.FILES, instance=cetegoriesedit)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Edit Goggles Category Successfully...")
            return redirect(request.META["HTTP_REFERER"])
    else:
        form = TypesForm(instance=cetegoriesedit)

    comtext = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "datetime": now,
        "cetegories_edit": cetegories_edit,
        "datetime": now,
        "cetegoriesedit": cetegoriesedit,
        "form": form,
    }
    return render(request, "categories_edit.html", comtext)


def CategoriesGogglesView(request, goggles_types_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    cetegories_view = Gogglestype.objects.filter(
        goggles_types_id=goggles_types_id
    ).values()
    goggles_view = Goggles.objects.filter(goggles_types_id=goggles_types_id).values()
    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "cetegories_view": cetegories_view,
        "goggles_view": goggles_view,
    }
    return render(request, "goggles_view.html", context)


def GoogleView(request, goggles_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    goggleview = Goggles.objects.filter(goggles_id=goggles_id).values()
    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "goggleview": goggleview,
    }
    return render(request, "goggle_view.html", context)


def GoogleEdit(request, goggles_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    goggle_edit = Goggles.objects.filter(goggles_id=goggles_id).values()
    now = datetime.datetime.now()
    goggleedit = Goggles.objects.get(goggles_id=goggles_id)

    goggles_form = GogglesForm(request.POST, request.FILES, instance=goggleedit)

    if request.method == "POST":
        if goggles_form.is_valid():
            goggles_form.save()
            messages.success(request, "Edit Goggles Successfully...")
            return redirect(request.META["HTTP_REFERER"])
    else:
        goggles_form = GogglesForm(instance=goggleedit)

    comtext = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "datetime": now,
        "goggle_edit": goggle_edit,
        "goggleedit": goggleedit,
        "goggles_form": goggles_form,
    }
    return render(request, "goggle_edit.html", comtext)


def GoogleDelete(request, goggles_id):
    google_delete = Goggles.objects.filter(goggles_id=goggles_id)
    google_delete.delete()
    messages.success(request, "Delete Goggle Successfully")
    return redirect("/add-product/")


def Img1(request, goggles_img1):
    gimg = Goggles.objects.get(goggles_img1=goggles_img1)
    gimg.goggles_img1 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img2(request, goggles_img2):
    gimg2 = Goggles.objects.get(goggles_img2=goggles_img2)
    gimg2.goggles_img2 = ""
    gimg2.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img3(request, goggles_img3):
    gimg = Goggles.objects.get(goggles_img3=goggles_img3)
    gimg.goggles_img3 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img4(request, goggles_img4):
    gimg = Goggles.objects.get(goggles_img4=goggles_img4)
    gimg.goggles_img4 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img5(request, goggles_img5):
    gimg = Goggles.objects.get(goggles_img5=goggles_img5)
    gimg.goggles_img5 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img6(request, goggles_img6):
    gimg = Goggles.objects.get(goggles_img6=goggles_img6)
    gimg.goggles_img6 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img7(request, goggles_img7):
    gimg = Goggles.objects.get(goggles_img7=goggles_img7)
    gimg.goggles_img7 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img8(request, goggles_img8):
    gimg = Goggles.objects.get(goggles_img8=goggles_img8)
    gimg.goggles_img8 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img9(request, goggles_img9):
    gimg = Goggles.objects.get(goggles_img9=goggles_img9)
    gimg.goggles_img9 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Img10(request, goggles_img10):
    gimg = Goggles.objects.get(goggles_img10=goggles_img10)
    gimg.goggles_img10 = ""
    gimg.save()
    messages.success(request, "Delete Image")
    return redirect(request.META["HTTP_REFERER"])


def Add_product(request):
    if request.session.has_key("email"):
        if request.method == "POST":
            goggles_form = GogglesForm(request.POST, request.FILES)
            if goggles_form.is_valid():
                goggles_form.save()
                messages.success(request, "ADD Goggles Successfully...")
                return redirect("/add-product/")
        else:
            goggles_form = GogglesForm()
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()
        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()
        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        now = datetime.datetime.now()
        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
            "datetime": now,
            "goggles_form": goggles_form,
        }
        return render(request, "admin_addproduct.html", context)
    else:
        return redirect("/dashboard-login/")


def Brands(request):
    if request.session.has_key("email"):
        if request.method == "POST":
            brand_form = BrandsForm(request.POST, request.FILES)
            if brand_form.is_valid():
                brand_form.save()
                messages.success(request, "ADD Brand Successfully...")
                return redirect("/dashboard/brands/")
        else:
            brand_form = BrandsForm()
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()

        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()

        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        now = datetime.datetime.now()
        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
            "datetime": now,
            "brand_form": brand_form,
        }
        return render(request, "admin_brands.html", context)
    else:
        return redirect("/dashboard-login/")


def BrandView(request, goggles_brand_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    brand_view = Gogglesbrand.objects.filter(goggles_brand_id=goggles_brand_id).values()
    goggles_view = Goggles.objects.filter(goggles_brand_id=goggles_brand_id).values()
    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "brand_view": brand_view,
        "goggles_view": goggles_view,
    }
    return render(request, "brand_view.html", context)


def BrandEdit(request, goggles_brand_id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    now = datetime.datetime.now()
    brand_edit = Gogglesbrand.objects.filter(goggles_brand_id=goggles_brand_id).values()
    brandedit = Gogglesbrand.objects.get(goggles_brand_id=goggles_brand_id)

    brand_form = BrandsForm(request.POST, request.FILES, instance=brandedit)
    if request.method == "POST":
        if brand_form.is_valid():
            brand_form.save()
            messages.success(request, "Edit Goggles Brand Successfully...")
            return redirect(request.META["HTTP_REFERER"])
    else:
        brand_form = BrandsForm(instance=brandedit)

    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "datetime": now,
        "brand_form": brand_form,
        "brand_edit": brand_edit,
        "brandedit": brandedit,
    }
    return render(request, "brand_edit.html", context)


def BrandDelete(request, goggles_brand_id):
    Brands_delete = Gogglesbrand.objects.filter(goggles_brand_id=goggles_brand_id)
    Brands_delete.delete()
    messages.success(request, "Delete Brand Successfully")
    return redirect("/dashboard/brands/")


def Coupons_modal(request):
    if request.session.has_key("email"):
        if request.method == "POST":
            coupons_form = CouponsForm(request.POST, request.FILES)
            if coupons_form.is_valid():
                coupons_form.save()
                messages.success(request, "ADD Coupons Successfully...")
                return redirect("/coupons/")
        else:
            coupons_form = CouponsForm()

        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()
        goggles_coupons = Coupons.objects.all()
        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()
        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        now = datetime.datetime.now()
        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "goggles_coupons": goggles_coupons,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
            "datetime": now,
            "coupons_form": coupons_form,
        }
        return render(request, "admin_conpons.html", context)
    else:
        return redirect("/dashboard-login/")


def CouponsView(request, coupon_code):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggles_coupons = Coupons.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    coupons_view = Coupons.objects.filter(coupon_code=coupon_code).values()
    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "goggles_coupons": goggles_coupons,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "coupons_view": coupons_view,
    }
    return render(request, "coupons_view.html", context)


def CouponsEdit(request, coupon_code):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    goggles_coupons = Coupons.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    now = datetime.datetime.now()
    coupons_edit = Coupons.objects.filter(coupon_code=coupon_code).values()
    couponsedit = Coupons.objects.get(coupon_code=coupon_code)

    coupons_form = CouponsForm(request.POST, request.FILES, instance=couponsedit)
    if request.method == "POST":
        if coupons_form.is_valid():
            coupons_form.save()
            messages.success(request, "Edit Goggles Coupons Successfully...")
            return redirect(request.META["HTTP_REFERER"])
    else:
        coupons_form = CouponsForm(instance=couponsedit)

    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "goggles_coupons": goggles_coupons,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "datetime": now,
        "coupons_form": coupons_form,
        "coupons_edit": coupons_edit,
        "couponsedit": couponsedit,
    }
    return render(request, "coupons_edit.html", context)


def CouponsDelete(request, coupon_code):
    CouponsDelete = Coupons.objects.filter(coupon_code=coupon_code)
    CouponsDelete.delete()
    messages.success(request, "Delete Coupons Successfully")
    return redirect("/coupons/")


def Users(request):
    if request.session.has_key("email"):
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()
        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()
        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        address = Address.objects.all()
        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
            "address": address,
        }
        return render(request, "admin_users.html", context)
    else:
        return redirect("/dashboard-login/")


def UserView(request, id):
    users = User.objects.all()
    goggless = Goggles.objects.all()
    goggles_type = Gogglestype.objects.all()
    goggles_brand = Gogglesbrand.objects.all()
    admin_user = UserAdmin.objects.all()
    users_count = User.objects.all().count()
    goggless_count = Goggles.objects.all().count()
    goggles_type_count = Gogglestype.objects.all().count()
    goggles_brand_count = Gogglesbrand.objects.all().count()
    goggles_coupons_count = Coupons.objects.all().count()
    email = UserAdmin.objects.filter(email=request.session["email"]).values()
    users_view = User.objects.filter(id=id).values()
    user_address = Address.objects.filter(userid=id).values()
    context = {
        "users": users,
        "goggless": goggless,
        "goggles_type": goggles_type,
        "goggles_brand": goggles_brand,
        "admin_user": admin_user,
        "users_count": users_count,
        "goggless_count": goggless_count,
        "goggles_type_count": goggles_type_count,
        "goggles_brand_count": goggles_brand_count,
        "goggles_coupons_count": goggles_coupons_count,
        "email": email,
        "users_view": users_view,
        "user_address": user_address,
    }
    return render(request, "user_view.html", context)


def Reviews(request):
    if request.session.has_key("email"):
        users = User.objects.all()
        goggless = Goggles.objects.all()
        goggles_type = Gogglestype.objects.all()
        goggles_brand = Gogglesbrand.objects.all()
        admin_user = UserAdmin.objects.all()
        users_count = User.objects.all().count()
        goggless_count = Goggles.objects.all().count()
        goggles_type_count = Gogglestype.objects.all().count()
        goggles_brand_count = Gogglesbrand.objects.all().count()
        goggles_coupons_count = Coupons.objects.all().count()
        email = UserAdmin.objects.filter(email=request.session["email"]).values()
        context = {
            "users": users,
            "goggless": goggless,
            "goggles_type": goggles_type,
            "goggles_brand": goggles_brand,
            "admin_user": admin_user,
            "users_count": users_count,
            "goggless_count": goggless_count,
            "goggles_type_count": goggles_type_count,
            "goggles_brand_count": goggles_brand_count,
            "goggles_coupons_count": goggles_coupons_count,
            "email": email,
        }
        return render(request, "admin_reviews.html", context)
    else:
        return redirect("/dashboard-login/")


def Admin_Logout(request):
    del request.session["email"]
    return redirect("/dashboard-login/")
