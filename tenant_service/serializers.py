from rest_framework import serializers
from .models import Tenant, Branch


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['name', 'schema_name', 'domain', 'created_at']
        read_only_fields = ['created_at']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
