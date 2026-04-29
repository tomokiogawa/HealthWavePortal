from django.urls import path
from . import views


app_name = "ltc"
urlpatterns = [
    path("", views.index, name="index"),
]