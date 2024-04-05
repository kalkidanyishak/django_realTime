from django.urls import path,include
from . import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('api/rooms/', chat_views.RoomListCreateAPIView.as_view(), name='room-list-create'),
    path('api/messages/', chat_views.ChatMessageListCreateAPIView.as_view(), name='message-list-create'),
]