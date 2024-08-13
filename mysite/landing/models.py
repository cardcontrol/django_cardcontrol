from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
    
class CustomUser(AbstractUser):

    # Add additional fields here
    first_name = models.CharField(max_length=30) 

    last_name = models.CharField(max_length=30)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customusers',  # Custom name for the relationship
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customusers',  # Custom name for the relationship
        blank=True,
        help_text='Specific permissions for this user.'
    )