from rest_framework import generics
from .models import Tenant, Branch
from .serializers import TenantSerializer, BranchSerializer
from db_config.tenant_router import TenantRouter

class TenantRegistrationView(generics.CreateAPIView):
    serializer_class = TenantSerializer
    
    def perform_create(self, serializer):
        tenant = serializer.save()
        TenantRouter().switch_schema(tenant.schema_name)

class BranchRegistrationView(generics.CreateAPIView):
    serializer_class = BranchSerializer
