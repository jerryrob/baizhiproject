from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
import random,string,os
from userapp.models import User
from userapp.image import ImageCaptcha

from django.contrib.auth.hashers import make_password, check_password

#Create your views here.
def register_page(request):

    return render(request,'user/register.html')

def register(request):

    username = request.POST.get("username")
    hobby = request.POST.getlist("hobby")
    realname = request.POST.get("realname")
    password = request.POST.get("password")
    gender = request.POST.get("gender")  # "1"   "0"
    birth = request.POST.get("birth")    # 规范日期格式
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    pwd = make_password(password, salt)  # 传入明文，返回密文(盐=随机的字符串)

    userPicFile = request.FILES.get('user_pic')  # 接收文件
    # print("文件原始名为：", userPicFile.name, " 文件类型为：", userPicFile.content_type)
    # 2.将数据存入数据库
    h=""
    for i in hobby:
        h+=i+" "
    if(userPicFile):
        User(username=username,hobby=h,realname=realname,password=pwd,salt=salt,gender=gender,birth=birth,pic=userPicFile).save()
    else:
        User(username=username, hobby=h, realname=realname, password=pwd,salt=salt, gender=gender, birth=birth).save()
    # 响应
    print("注册成功~~~~")
    return redirect("user:loginp")
def check_username(request):
    username = request.GET.get("username")
    if(not username):
        return HttpResponse("1")
    user=User.objects.filter(username=username)
    if(user):
        #用户名已存在！
        return HttpResponse("1")
    else:
        return HttpResponse("0")
def check_code(request):
    checkcode=request.GET.get("checkcode")
    realcode = request.session.get("realcode")
    print("realcode:", realcode)
    if (checkcode and realcode and checkcode.lower() == realcode.lower()):
        return HttpResponse("0")
    else:
        return HttpResponse("1")

def login_page(request):
    if request.session.get("msg"):
        del request.session["msg"]
    username=request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    # pwd2 = make_password("1234",salt="xxxxx")# 传入明文和盐，返回密文
    return render(request, 'user/login.html',{"username":username,"password":password})

def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    remember = request.POST.get("remember")
    checkcode   = request.POST.get("checkcode")
    print(username,password)
    res=redirect("dept:deptquery")
    if remember=="1":
        expire=60 * 60 * 24*7
        res.set_cookie("username",username,max_age=expire)  # key="name"  value="zhj"
        res.set_cookie("password", password,max_age=expire)  # key="name"  value="zhj"
        res.set_cookie("remember", remember,max_age=expire)
        #res.set_cookie("password", "123", max_age=60 * 60 * 24)  # cookie存活1day
    else:
        res.delete_cookie("username")
        res.delete_cookie("password")
        res.delete_cookie("remember")
        res.delete_cookie("realcode")
        request.session.flush()
        request.session.clear()
    date=User.objects.filter(username=username)
    msg=""
    if(date):
        user=date[0]
        if(user.username== username and check_password(password,user.password)):
            msg = "登录成功！"
            # 记录用户登录状态
            request.session['username'] = user.username
            if (user.pic):
                request.session['pic'] = user.pic.url
            else:
                request.session['pic'] = 'user_pic/head.png'
            return res
    else:
        msg = "用户或密码错误！"
        print(msg)
    request.session['msg'] = msg
    return render(request, 'user/login.html',{"msg":msg})
def test(request):

    return render(request, 'user/login.html')

def generate_captcha(request):
    """
    制作验证码图片，并写出给浏览器
    :param request:
    :return:
    """
    path = os.path.abspath("cap/fonts/verdana.ttf")#对给定文件名前加上当前工作目录的绝对路径
    print("path:",path)
    #创建了ImageCaptcha对象，并设置了字体
    image_cap = ImageCaptcha(fonts=[path])
    #随机生成5位验证码
    code_list = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    code_str = "".join(code_list)
    print("code:",code_str)
    #将码值  存入session，保持，以供后续比对
    request.session["realcode"] = code_str
    #将码值  画到一张图片中
    data = image_cap.generate(code_str)
    print("data:",data,type(data))

    return HttpResponse(data,"image/png")

def ajaxPage(request):
    return render(request, 'user/test.html')
def ajax_test1(request):
    name=request.GET.get("name")
    age=request.GET.get("age")
    print(name,age)
    return HttpResponse("这里是get响应！")
def ajax_test2(request):
    name=request.POST.get("name")
    age=request.POST.get("age")
    print(name,age)
    return HttpResponse("这里是post响应！")

def json_page(request):
    return render(request,"test/ta.html")
def json_test1(request):


    users=list(User.objects.all().values())
    def mydefault(d):  # d = 需要转换格式的数据 = user
        for u in users:
            if isinstance(u.get("create_time"), datetime):  # 判断是否为日期数据
                # 返回格式化的数据
                return u.get("create_time").strftime("%Y-%m-%d")
                # JsonResponse会将user转换为json，然后输出给client

    return JsonResponse({"users": users}, json_dumps_params={"default": mydefault})
    #或者
    #return JsonResponse(users,safe=False)#k添加safe=False,可以不是字典类型，解析json字符串时eval不用加（）包裹
    # return JsonResponse({"users":users})
    #return HttpResponse("这里是post响应！")

def ajax_page1(request):
    name=request.POST.get("name")
    age=request.POST.get("age")
    print(name,age)
    return HttpResponse("这里是响应！")
def ajax_page2(request):
    pass

def index(request):
    return render(request,"index.html")