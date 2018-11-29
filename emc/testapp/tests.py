import os
from django.test import TestCase
from django.db import  transaction
import django
from django.db import transaction
import traceback

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emc.settings")
django.setup()
# Create your tests here.
from testapp.models import Category,Goods,Student,Course,Person,Passport
def testOneToMany():
    #获取类别
    # cates=Category.objects.all()
    #
    # print(type(cates[1].goods_set),type(Category.objects))
    #
    # c=cates[1].goods_set.filter(gprice__gt=300)
    # c2 = cates[1].goods_set.all()
    # for i in c:
    #     print(i.gtitle, i.gprice)
    #
    # for i in c2:
    #     print(i.gtitle, i.gprice)
    #print(goods)
    g = Goods.objects.all()
    # for i in g:
    #     print(i.gtitle,i.gprice)
    # print(g[0].fk_cg,g[0].fk_cg.id,g[0].fk_cg.title)
    good=Goods.objects.filter(fk_cg_id__gte=2)
    goods = Goods.objects.filter(fk_cg__title__contains='电').values('fk_cg__title','id','gtitle')
    print(list(goods))

    c1=Category.objects.filter(goods__gtitle__contains='相机')
    #print(c1[0].goods_set)
    c2=Category.objects.filter(goods__gprice__gt=600)
    cs=list(set(c2))
    print(cs)
    for i in cs:
        print(i.title,i.create_time,list(i.goods_set.all()))
def testManyToMany():
    stus = Student.objects.all()
    a1=stus[0].course_set.all()  # 返回ManyRelatedManager，但并未查询数据
    print(type(stus[0].course_set),list(a1))

    a2=stus[0].course_set.filter(coursename__contains='线')
    la=list(a2)
    print(la[0].coursename)

    cour=Course.objects.all()
    c1=cour[0].students.all()
    #print(type(cour[0].students),type(c1))
    #print(list(c1))
    # for i in c1:
    #     print(i.id,i.name,i.gender)
    # s2=cour[0].students.filter(name__contains='张三')
    #print(list(s2.all()))
    # #获得第一个学生的 标题中含有"s"的课程#查询一方：
    # Coursecours = Course.objects.all()
    # cours[0].students.all()
    # cours[0].students.filter(age__gt=18)#关联查询：以课程为条件 查询学生
    # Student.objects.filter(course__title__contains="h") #标题中含有"h"的课程中的学生Student.objects.filter(course__expire__gt=2) #课时大于2的课程中的学生#关联查询：以学生为条件 查询课程Course.objects.filter(students__name="zzz") #姓名为zzz的学生参加的课程Course.objects.filter(students__age__gt=18) #年龄大于18的学生参加的课程
    s3=Student.objects.filter(course__coursename__contains='线').all()
    s4 = Student.objects.filter(course__expire__gt=3).all()
    print(list(s3),list(s4))
    c3=Course.objects.filter(students__name__contains='张三').all()
    print(list(c3))
def testoneToOne():
    per=Person.objects.all()
    pass1=per[0].passport
    print(pass1,pass1.expire)
    pa=Passport.objects.all()
    print(pa[0].per.id,pa[0].per.name)
    p1=Person.objects.filter(passport__expire__gt=3).all()
    print(list(p1))
    pa2=Passport.objects.filter(per__age__gt=18)
    s1=list(pa2)
    print(s1[0].note)

def addTest():
    # c=Category.objects.get(id=1)
    # g=Goods(gtitle='耳机',gprice=1200,fk_cg=c)
    # g.save()
    c2=Category.objects.get(id=1)
    c2.goods_set.create(gtitle='MP3',gprice=200,fk_cg=c2)
def testTransaction():
    try:
        with transaction.atomic():
            Person(name="a1",age=20).save()
            Person(name="a2",age=18).save()
            Person(name="a3", age=30).save()
            print("success！")
    except ValueError as e:
        print(e)
        traceback.print_exc()
def saveOneToOnetest():
    # c=Category.objects.get(id=3)
    # #g=Goods(gtitle="zzz6",gprice=6000,fk_cg=c)
    # c.goods_set.create(gtitle="服装1",gprice=5000)
    #

    c=Category(title='玩具2',create_time="2018-12-09")
    c.save()
    g = Goods(gtitle='汽车2', gprice=200)
    g.save()
    c.goods_set.add(g)
def testTransaction():

    with transaction.atomic():
        Category(title='玩具e', create_time="2018-12-09").save()
        Category(title='玩具f', create_time="2018-12-09").save()
        a=1/0
import datetime
def t():
    d1='2018-11-10'
    d2='2018-11-11'
    date = datetime.datetime.strptime(d1,'%Y-%m-%d')
    print(date,type(date),type(datetime.datetime.now()))

if __name__=="__main__":
    t()


