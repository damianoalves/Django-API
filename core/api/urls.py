from django.urls import path
from rest_auth.views import UserDetailsView, PasswordChangeView

from core.api.viewsets import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='rest_register'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
]