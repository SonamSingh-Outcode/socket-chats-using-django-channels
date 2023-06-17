from django.urls import path
from . import views


urlpatterns = [
   path("", views.home_view, name="home"),
   path("rooms/<uuid:uuid>/", views.room_chat_view, name="room")
]