from django.db import models

# Models
from applications.users.models import Users

# Create your models here.
class posts(models.Model):
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.BooleanField()
    class Meta:
        abstract = True

class avisos(posts):
    image = models.ImageField(upload_to='uploads/avisos/% Y/% m/% d/')


class menu_comida(posts):
    image = models.ImageField(upload_to='uploads/comida/% Y/% m/% d/')


class transporte_rutas(posts):
    image = models.ImageField(upload_to='uploads/transporte/% Y/% m/% d/')
