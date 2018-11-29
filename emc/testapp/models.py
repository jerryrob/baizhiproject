from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=20)
    create_time=models.DateField(auto_now_add=True)
    class Meta:
        db_table="t_category"
class Goods(models.Model):
    gtitle=models.CharField(max_length=20,unique=True)
    gprice=models.FloatField(db_column='price')
    fk_cg=models.ForeignKey(to=Category,on_delete=models.CASCADE,db_column='cate_id')
    class Meta:
        db_table="t_goods"
class Student(models.Model):
    name=models.CharField(max_length=30,null=False)
    age=models.SmallIntegerField
    gender=models.NullBooleanField()
    sid=models.CharField(max_length=20)

    class Meta:
        db_table = "t_student"
class Course(models.Model):
    coursename=models.CharField(max_length=30,null=False)
    expire=models.SmallIntegerField()

    # 关系属性
    # 1.关系双方   2.关系的外键(省略)  3.on_delete(不支持)
    students=models.ManyToManyField(to=Student)
    class Meta:
        db_table = "t_course"

class Person(models.Model):
    name = models.CharField(max_length=20,unique=True)
    age = models.SmallIntegerField()
    class Meta:
        db_table="t_person"

class Passport(models.Model):
    note = models.CharField(max_length=20)
    expire = models.SmallIntegerField()
    #关系属性：描述关系
    #1.关系双方  2.关系外键   3.on_delete
    per=models.OneToOneField(to=Person,db_column="person_id",on_delete=models.CASCADE)
    class Meta:
        db_table = "t_passport"
