from django.db import models

# Create your models here.

class Films(models.Model):
    title=models.CharField(max_length=120,null=False)
    actor=models.CharField(max_length=120,null=True)
    image = models.CharField(max_length=150, null=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    time=models.CharField(max_length=80,null=True)
    index=models.IntegerField()
    class Meta:
        db_table="t_films"


