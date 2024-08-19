from django.urls import path
from .views import GatewayAPIView

urlpatterns = [
    path('', GatewayAPIView.as_view(), name='api-gateway'),
]
