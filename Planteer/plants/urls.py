from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("all/", views.all_view, name="all_view"),
    path("<plant_id>/detail/", views.detail_view, name="detail_view"),
    path("new/", views.new_view, name="new_view"),
    path("<plant_id>/update/", views.update_view, name="update_view"),
    path("<plant_id>/delete/", views.delete_view, name="delete_view"),
    path("search/", views.search_view, name="search_view")
]
