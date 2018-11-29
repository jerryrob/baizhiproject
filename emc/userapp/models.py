from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, null=False,unique=True)
    password = models.CharField(max_length=150, null=False)
    salt = models.CharField(max_length=20, null=False)
    realname = models.CharField(max_length=30, null=False)
    gender = models.NullBooleanField()
    hobby= models.CharField(max_length=200,default="",null=True)
    birth = models.DateField(default=None,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    pic = models.ImageField(upload_to="user_pic",default="user_pic/head.png")
    class Meta:
        db_table="t_user"
