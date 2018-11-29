from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=20)
    note = models.CharField(max_length=200)

    class Meta:
        db_table="t_department"

