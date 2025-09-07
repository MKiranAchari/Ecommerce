from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile
from orders.models import Order


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

def logout(request):
    return render(request, "accounts/logout.html")

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    if request.method == "POST":
        profile.address = request.POST.get("address")
        profile.phone = request.POST.get("phone")
        profile.save()
        return redirect("profile")

    return render(request, "accounts/profile.html", {
        "profile": profile,
        "orders": orders,
    })
