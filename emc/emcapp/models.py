from django.db import models

from dept.models import  Department
# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30,null=False)
    age=models.IntegerField(null=True)
    gender=models.NullBooleanField()
    salary=models.DecimalField(max_digits=12,decimal_places=2,null=True)
    birth=models.DateField(null=True)
    create_time=models.DateTimeField(auto_created=True)
    modify_time=models.DateTimeField(null=True)
    is_deleted=models.BooleanField(default=False)
    dept = models.ForeignKey(to=Department, on_delete=models.Empty,null=True,db_column='dept_id')

    class Meta:
        db_table = "t_emp"
