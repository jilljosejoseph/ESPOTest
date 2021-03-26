from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("item/add", views.add_item),
    path("items/<int:item_id>", views.item_display),
    path("items/<int:item_id>/delete", views.delete_item),
]