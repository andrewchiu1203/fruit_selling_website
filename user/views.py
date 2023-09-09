from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls.base import reverse_lazy
from user.models import Shoppingcart, Order
from product.models import Product, Season

# Create your views here.
def blank(request):
    url = reverse_lazy('user:index')
    return redirect(url)

def index(request):
    if not request.user.is_authenticated:
        return render(request, "user/Index.html")
    else:
        return render(request, "user/Index_signin.html")

def shoppingcart(request):
    if not request.user.is_authenticated:
        url = reverse_lazy("user:signin")
        return redirect(url)
    else:
        if request.method == "POST":
            try:
                username = request.user.username
                number = request.POST["number"]
                id = request.POST["product_id"]
            except:
                try:
                    # if number not found but product id found, it means user presses the delete button
                    id = request.POST["product_id"]
                    username = request.user.username
                    user = Shoppingcart.objects.get(user = username, product = Product.objects.get(id = id))
                    user.delete_product(username, Product.objects.get(id = id))
                    user = Shoppingcart.objects.filter(user = request.user.username)
                    return render(request, "product/Shoppingcart.html", {"user": user})
                    
                except:
                    # if number not found and product id also not found, it means user presses the send order button
                    address = request.POST['address']
                    username = request.user.username
                    timezone = request.POST['timezone']
                    date = request.POST['time']
                    # date = str(datetime.datetime.now())
                    if address == "":
                        user = Shoppingcart.objects.filter(user = request.user.username)
                        return render(request, "product/Shoppingcart.html", {"user": user, "error": "  不得輸入空白地址  "})
                    else:
                        for u in Shoppingcart.objects.filter(user = username):
                            Order.send_order(username, u.product, u.number, address, date, timezone)

            else:
                # if number and product id are both found, user must have pressed the modify button to edit shoppintcart
                username = request.user.username
                number = request.POST["number"]
                id = request.POST["product_id"]
                user = Shoppingcart.objects.filter(user = request.user.username)
                # can't enter empty
                if number == "":
                    return render(request, "product/Shoppingcart.html", {"user": user, "error": "  無法輸入空白  "})
                # can't enter zero or negative
                if int(number) <= 0:
                    return render(request, "product/Shoppingcart.html", {"user": user, "error": "  公斤數不得小於或等於零  "})
                
                user = Shoppingcart.objects.get(user = username, product = Product.objects.get(id = id))
                user.update_number(username, Product.objects.get(id = id), number)


            user = Shoppingcart.objects.filter(user = request.user.username)
            return render(request, "product/Shoppingcart.html", {"user": user})
        else:
            user = Shoppingcart.objects.filter(user = request.user.username)
            return render(request, "product/Shoppingcart.html", {"user": user})

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return render(request, "user/Signin_successfully.html")
        elif username == "" or password == "":
            return render(request, "user/Sign_in.html", {"message": "請填滿所有欄位"})
        else:
            return render(request, "user/Sign_in.html", {"message": "輸入的密碼或帳號不正確"})
    
    else:
        if request.user.is_authenticated:
            url = str(reverse_lazy('user:index'))
            return redirect(url)
        else:
            return render(request, "user/Sign_in.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]
        email = request.POST["email"]

        if username == "" or password == "" or re_password == "" or email == "":
            return render(request, "user/Sign_up.html", {"message": "請填滿所有欄位"})

        if password == re_password:
            if list(User.objects.filter(username = username)) != []:
                return render(request, "user/Sign_up.html", {"message": "此帳號名稱已經存在"})
            
            if list(User.objects.filter(email = email)) != []:
                return render(request, "user/Sign_up.html", {"message": "此Email帳號已經存在"})

            user = authenticate(request, username = username, password = password, email = email)
            if user is not None:
                return render(request, "user/Sign_up.html", {"message": "此帳號已經存在，請回首頁登入"})
            else:
                user = User.objects.create_user(username = username, password = password, email = email)
                user.save()
                return render(request, "user/Signup_successfully.html")
        else:
            return render(request, "user/Sign_up.html", {"message": "請輸入相同的密碼"})
    else:
        if request.user.is_authenticated:
            url = str(reverse_lazy('user:index'))
            return redirect(url)
        else:
            return render(request, "user/Sign_up.html")

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "user/Signout_successfully.html")
    else:
        url = str(reverse_lazy('user:index'))
        return redirect(url)

def order(request):
    if not request.user.is_authenticated:
        url = reverse_lazy("user:signin")
        return redirect(url)
    else:
        if request.method == "POST":
            username = request.user.username
            id = request.POST["product_id"]
            order_id = request.POST["order_id"]
            Order.delete_order(username, Product.objects.get(id = id), order_id)
            url = reverse_lazy("user:order")
            return redirect(url)
        else:
            return render(request, "product/Order.html", {"order": Order.objects.filter(user = request.user.username)})

def sort_season(request):
    if request.method == "POST":
        season = request.POST["season"]
        if season == "全部":
            url = str(reverse_lazy('product:index_no_season'))
            return redirect(url)
        else:
            # get the url of the product index page but replace the default "/all" with the season followed at the end
            url = str(reverse_lazy('product:index_no_season')).replace('/all', '') + f"/{season}"
            return redirect(url)
    else:
        return render(request, "user/Sort_season.html", {"season": Season.objects.all()})

def aboutus(request):
    if request.method == "POST":
        time = request.POST["time"]
        print(time)
        return render(request, "user/aboutus.html")
    else:
        return render(request, "user/aboutus.html")