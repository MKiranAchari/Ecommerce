from django.urls import path
from . import views


urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("history/", views.order_history, name="order_history"),
    path("payment/<int:order_id>/", views.payment, name="payment"),
]