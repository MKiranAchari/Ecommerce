from django.urls import path
from . import views

urlpatterns = [
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("", views.view_cart, name="view_cart"),
    path("update/<int:item_id>/<str:action>/", views.update_quantity, name="update_quantity"),
    path("remove/<int:item_id>/", views.remove_item, name="remove_item"),
]
