from django.urls import path, include
from django.shortcuts import redirect
from . import views


urlpatterns = [
   path('', lambda req: redirect('accounts/login')),
   path("home", views.home_view, name="home"),
   path("rooms/<uuid:uuid>/", views.room_chat_view, name="room"),
   path("accounts/", include("django.contrib.auth.urls")),
]