from functools import wraps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def get_role(user):
    if user.role:
        return user.role.role_name
    if user.is_superuser:
        return "Landlord"
    return None


def role_required(*roles):
    def decorator(view):
        @login_required
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            if get_role(request.user) in roles:
                return view(request, *args, **kwargs)
            messages.error(request, "You are not allowed to open that page.")
            return redirect("dashboard")
        return wrapper
    return decorator