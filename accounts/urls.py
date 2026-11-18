from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
        path("login/", auth_views.LoginView.as_view(
        template_name="accounts/login.html",
        authentication_form=LoginForm,
        redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/landlord/", views.landlord_dashboard, name="landlord_dashboard"),
    path("dashboard/caretaker/", views.caretaker_dashboard, name="caretaker_dashboard"),
    path("dashboard/tenant/", views.tenant_dashboard, name="tenant_dashboard"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
]