from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from product.models import Product
from product.models import Season
from user.models import Shoppingcart

def index(request, season):
    if request.method == "POST":
        if not request.user.is_authenticated:
            url = str(reverse_lazy('user:signin'))
            return redirect(url)
        else:
            number = request.POST["number"]
            id = request.POST["product_id"]
            user_name = request.user.username

            # can't enter empty number
            if number == "":
                if season == "all":
                    return render(request, "product/Index.html", {"products": Product.objects.all(), "error": "  無法輸入空白  ", "season": "全部"})
                else:
                    return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "error": "  無法輸入空白  ", "season": season})

            # can't enter zero or negative
            if int(number) <= 0:
                if season == "all":
                    return render(request, "product/Index.html", {"products": Product.objects.all(), "error": "  公斤數不得小於或等於零  ", "season": "全部"})
                else:
                    return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "error": "  公斤數不得小於或等於零  ", "season": season})

            # modify user's shoppingcart
            if id is not None and user_name is not None:
                # if user not found in shoppingcart, create new shoppingcart with current user's name and chosen product
                if list(Shoppingcart.objects.filter(user = user_name)) == []:
                    Shoppingcart.objects.create(product = Product.objects.get(id = id), number = number, user = user_name)
                    if season == "all":
                            return render(request, "product/Index.html", {"products": Product.objects.all(), "error": "", "season": "全部"})
                    else:
                        return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "error": "", "season": season})
                else:
                    try:
                        user = Shoppingcart.return_users_order_same_product(user_name, Product.objects.get(id = id))
                    except:
                        # if user found in shoppintcart but with different fruit, add new shoppingcart with current user's name and chosen product
                        Shoppingcart.objects.create(product = Product.objects.get(id = id), number = number, user = user_name)
                        if season == "all":
                            return render(request, "product/Index.html", {"products": Product.objects.all(), "error": "", "season": "全部"})
                        else:
                            return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "error": "", "season": season})
                    else:
                        # if user found in shoppingcart and same product is already in their, accumulate the number
                        sum = int(number) + int(user.number)
                        user.update_number(user_name, Product.objects.get(id = id), sum)
                        if season == "all":
                            return render(request, "product/Index.html", {"products": Product.objects.all(), "error": "", "season": "全部"})
                        else:
                            return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "error": "", "season": season})
            else:
                return render(request, "product/Index.html", {"products": Product.objects.all(), "season": season})
    else:
        if request.user.is_authenticated:
            if season == "all":
                return render(request, "product/Index.html", {"products": Product.objects.all(), "season": "全部"})
            else:
                return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "season": season})
        else:
            if season == "all":
                return render(request, "product/Index.html", {"products": Product.objects.all(), "no_user": "尚未登入", "season": "全部"})
            else:
                return render(request, "product/Index.html", {"products": Product.objects.filter(season = Season.objects.get(season_name = season)), "no_user": "尚未登入", "season": season})