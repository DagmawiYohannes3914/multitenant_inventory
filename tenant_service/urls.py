from django.urls import path
from .views import TenantRegistrationView, BranchRegistrationView

urlpatterns = [
    path('register/', TenantRegistrationView.as_view(), name='tenant-register'),
    path('branch/register/', BranchRegistrationView.as_view(),
         name='branch-register'),
]
