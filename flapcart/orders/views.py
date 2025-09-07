from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem
from django.http import HttpResponse


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect("view_cart")

    order = Order.objects.create(user=request.user)
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )
    cart_items.delete()  # Empty the cart after checkout
    return redirect("payment", order_id=order.id)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/order_history.html", {"orders": orders})

@login_required
def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == "POST":
        # For now, simulate successful payment
        order.payment_status = "paid"
        order.status = "completed"
        order.save()
        return redirect("order_history")
    return render(request, "orders/payment.html", {"order": order})
