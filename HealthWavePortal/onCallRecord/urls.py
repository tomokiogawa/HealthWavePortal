from django.urls import path
from . import views


app_name = "onCallRecord"
urlpatterns = [
    path("", views.index, name="index"),
]