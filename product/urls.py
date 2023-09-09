from django.http import request
from . import views
from django .urls import path

app_name = "product"
urlpatterns = [
    path("index/<str:season>", views.index, name = "index"),
    path("index/all", views.index, name = "index_no_season"),

    path("index/春季", views.index, name = "spring"),
    path("index/夏季", views.index, name = "summer"),
    path("index/春季", views.index, name = "fall"),
    path("index/冬季", views.index, name = "winter"),
]