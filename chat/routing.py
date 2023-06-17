from django.urls import  path

from . import consumers

websocket_urlpatterns = [
    path('', consumers.JoinAndLeave.as_asgi()),
    path('rooms/<uuid:uuid>/', consumers.RoomConsumer.as_asgi())

]