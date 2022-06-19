from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mine", views.mine, name="mine"),
    path("<str:name>", views.greet, name="greet")


]