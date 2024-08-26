from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Tenant, Branch
from .serializers import TenantSerializer, BranchSerializer
from db_config.tenant_router import TenantRouter
from .utils import create_schema


class TenantRegistrationView(generics.CreateAPIView):
    serializer_class = TenantSerializer

    def perform_create(self, serializer):
        tenant_name = serializer.validated_data.get('name')
        domain = f"{tenant_name.lower().replace(' ', '')}.myapp.com"

        if Tenant.objects.filter(domain=domain).exists():
            raise ValidationError("A tenant with this domain already exists.")

        tenant = serializer.save(domain=domain)
        create_schema(tenant.schema_name)
        TenantRouter().switch_schema(tenant.schema_name)


class BranchRegistrationView(generics.CreateAPIView):
    serializer_class = BranchSerializer
