from django.db import models

# Models
from applications.roles.models import Roles

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    created = models.DateField( auto_now_add=True)
