from django.conf import settings
from django.db import connection


class TenantRouter:
    def set_tenant(self, tenant_name):
        connection.set_schema(tenant_name)

    def get_tenant(self):
        return connection.get_schema()

    def switch_schema(self, tenant_name):
        if tenant_name not in settings.ALLOWED_TENANTS:
            raise Exception(f"Unknown tenant: {tenant_name}")
        self.set_tenant(tenant_name)
