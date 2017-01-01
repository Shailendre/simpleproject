from django.db import models

# Create your models here.
class UserModel(models.Model):
    firstName   = models.CharField(max_length = 30)
    lastName    = models.CharField(max_length = 30)
    email       = models.CharField(max_length = 50)
    password    = models.CharField(max_length = 50)

    class Meta:
        db_table = 'users'
