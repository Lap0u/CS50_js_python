from django.urls import path

from . import views,util

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.getPage, name="get")
]
