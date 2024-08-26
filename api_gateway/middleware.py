from django.db import connection
from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
from tenant_service.models import Tenant


class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tenant = self.get_tenant_from_request(request)
        if tenant:
            schema_name = tenant.schema_name
            self.set_tenant_schema(schema_name)
        else:
            self.set_tenant_schema('public')

    def get_tenant_from_request(self, request):

        hostname = request.get_host().split(':')[0].lower()

        tenant = Tenant.objects.filter(domain=hostname).first()

        if not tenant:
            raise Http404("Tenant does not exist.")

        return tenant

    def set_tenant_schema(self, schema_name):
        connection.set_schema(schema_name)
