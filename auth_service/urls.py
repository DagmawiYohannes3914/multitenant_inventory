from django.urls import path
from .views import UserRegistrationView, LoginView, RefreshTokenView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token-refresh'),
]
