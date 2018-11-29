from django.shortcuts import render, redirect,HttpResponse
from django.core.paginator import Paginator
from emcapp.models import Emp
from userapp.models import User
from dept.models import Department
# Create your views here.

def emp_detail(request):

    # 要查询第num页（从1开始）
    deptId = request.GET.get("deptId")
    if(deptId):
        request.session["deptId"]=deptId
    else:
        deptId=request.session["deptId"]

    num = request.GET.get("num")
    if not num:
        num=1
    size=3
    #查询部门信息
    dept=Department.objects.get(id=deptId)
    # 当前页的对象
    page = Paginator(Emp.objects.filter(dept_id=deptId), size).page(num)
    return render(request, 'emp/emplist.html',{"dept":dept,"page": page})

def emp_add_page(request):

    return render(request, 'emp/addEmp.html')

def emp_add(request):
    # //检查姓名是否存在
    name = request.POST.get("name")
    user=User.objects.filter(username=name)
    if(user):
        msg="姓名已经存在！"
        return HttpResponse(msg)

    deptId = request.session.get("deptId")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    birth = request.POST.get("birth")
    salary = request.POST.get("salary")
    #查询部门
    dept=Department.objects.get(id=deptId)

    e=Emp(dept=dept,name=name, age=age, gender=gender, birth=birth, salary=salary,create_time="2019-09-18",modify_time="2019-09-19",is_deleted=0)
    e.save()
    return redirect("/empapp/emp/detail/?deptId="+deptId+"&num=1")#

def emp_update_page(request):

    id = request.GET.get("id")
    date=Emp.objects.filter(id=id)
    if(date):
        return render(request, 'emp/updateEmp.html', {"emp": date[0]})

#@require_http_methods(["GET"，"POST"]) #此View，接收Get请求和POST请求
def emp_update(request):

    id = request.POST.get("id")
    name = request.POST.get("name")
    age= request.POST.get("age")
    gender = request.POST.get("gender")
    birth = request.POST.get("birth")
    salary = request.POST.get("salary")

    date = Emp.objects.get(id=id)
    date.name = name
    date.age = age
    date.gender = gender
    date.birth = birth
    date.salary = salary
    date.save()
    deptId = request.session["deptId"]
    return redirect("/empapp/emp/detail/?deptId=" + deptId + "&num=1")  #

def emp_delete(request):

    id=request.GET.get("id")
    Emp.objects.get(id=id).delete()
    deptId = request.session["deptId"]
    return redirect("/empapp/emp/detail/?deptId=" +deptId + "&num=1")  #