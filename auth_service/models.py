from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    ADMIN = 'admin'
    MANAGER = 'manager'
    STAFF = 'staff'
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    # Override the groups field to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name to avoid conflict
        blank=True,
        help_text=('The groups this user belongs to. '
                   'A user will get all permissions granted to each of '
                   'their groups.'),
        related_query_name='customuser',
    )

    # Override the user_permissions field to avoid conflicts
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        # Custom related name to avoid conflict
        related_name='customuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
    
        
    
    
