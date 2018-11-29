from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from userapp.models import  User
# Create your views here.
def suggest(request):
    return render(request,"ajax/suggest.html")

def suggestCon(request):
    #t=['ajax','Json','Web','Webkit','Django','js','jQuery','html']
    name=request.POST.get("name")
    print(name)
    users=list(User.objects.filter(username__contains=name).values("username"))
    return JsonResponse(users, safe=False)
def upload(request):
    return render(request,"ajax/fileUpload.html")
def uploadFile(request):
    file = request.FILES.get('source')
    print("文件原始名为：", file.name, " 文件类型为：", file.content_type, type(file))

    u=User.objects.get(id=1)
    u.username="wewe"
    u.pic=file
    u.save()
    print(u.pic.url)
    return HttpResponse(u.pic.url)  # 文件的保存路径为响应内容