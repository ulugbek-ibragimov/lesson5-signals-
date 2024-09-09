from django.urls import path
from apps.users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView, UserProfileRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/<int:pk>/profile/', UserProfileRetrieveUpdateDestroyAPIView.as_view()),
]