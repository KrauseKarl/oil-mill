from django.urls import path
from .views import index, about

app_name = "shop"

urlpatterns = [
    path("", index, name="main"),
    path("about", about, name="about"),
]