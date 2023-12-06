from django.urls import path
from . import views

urlpatterns = [
    # path("accounts/", views.accounts),
    path("add-education/", views.add_edu, name="add-education"),
    path("add-experience/", views.add_exp, name="add-experience"),
    path("create-profile/", views.create, name="create-profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("profiles/", views.profiles, name="profiles"),
    path("register/", views.register, name="register"),
]
