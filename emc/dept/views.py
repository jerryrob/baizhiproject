from django.shortcuts import render,redirect

from dept.models import Department
# Create your views here.
def dept_list(request):
    depts=Department.objects.all()
    pic = request.session.get("pic")
    username = request.session.get("username")
    return render(request,'dept/departmentlist.html',{"username":username,"user_pic":pic,"depts":depts})

def add_page(request):

    return render(request, 'dept/addDepartment.html')

def add(request):
    name=request.POST.get("name")
    note = request.POST.get("note")
    dept=Department(name=name,note=note)
    dept.save()
    return redirect("dept:deptquery")

def update_page(request):

    id=request.GET.get("id")
    dept=Department.objects.get(id=id)
    return render(request, 'dept/updateDept.html',{"dept":dept})

def update(request):
    id = request.POST.get("id")
    name=request.POST.get("name")
    note=request.POST.get("note")

    dept=Department.objects.get(id=id)
    dept.name=name
    dept.note=note
    dept.save()
    return redirect("dept:deptquery")

def del_dept(request):

    id = request.GET.get("id")
    Department.objects.get(id=id).delete()
    return redirect("dept:deptquery")