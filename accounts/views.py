from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from .decorators import role_required, get_role


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
        messages.error(request, "Please fix the errors below.")
    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    target = {
        "Landlord": "landlord_dashboard",
        "Caretaker": "caretaker_dashboard",
        "Tenant": "tenant_dashboard",
    }.get(get_role(request.user))
    if target:
        return redirect(target)
    return render(request, "accounts/no_role.html")


@role_required("Landlord")
def landlord_dashboard(request):
    return render(request, "accounts/landlord_dashboard.html")


@role_required("Caretaker")
def caretaker_dashboard(request):
    return render(request, "accounts/caretaker_dashboard.html")


@role_required("Tenant")
def tenant_dashboard(request):
    return render(request, "accounts/tenant_dashboard.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def profile_edit(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        messages.error(request, "Please fix the errors below.")
    return render(request, "accounts/profile_edit.html", {"form": form})