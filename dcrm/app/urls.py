from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.record_details, name="record"),
    path("delete/<int:pk>", views.delete_record, name="delete"),
    path("edit/<int:pk>", views.edit_record, name="edit_record"),
    path("add_record/", views.add_record, name="add_record"),

]
