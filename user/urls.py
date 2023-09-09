from . import views
from django .urls import path

app_name = "user"
urlpatterns = [
    path("", views.blank, name="blank"),
    path("index/", views.index, name = "index"),
    path("signin/", views.signin, name = "signin"),
    path("signup/", views.signup, name = "signup"),
    path("signout/", views.signout, name = "signout"),
    path("shoppingcart/", views.shoppingcart, name = "shoppingcart"),
    path("order/", views.order, name = "order"),
    path("sort_season/", views.sort_season, name = "sort_season"),
    path("about_us/", views.aboutus, name="aboutus"),
]