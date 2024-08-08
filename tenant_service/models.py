from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    schema_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Branch(models.Model):
    tenant = models.ForeignKey(
        Tenant, related_name='branches', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
