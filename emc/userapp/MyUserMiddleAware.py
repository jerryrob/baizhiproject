from django.conf import settings
from django.shortcuts import redirect,render
from django.utils.deprecation import MiddlewareMixin

class MyMiddleAware(MiddlewareMixin):
    def __init__(self,get_response):#初始化
        super().__init__(get_response)
        print("init11")
	#view处理请求前执行
    def process_request(self,request):
        print("request11:",request)
    #在process_request之后View之前执行
    def process_view(self,request, view_func, view_args, view_kwargs):
        print("view11:",request,view_func,view_args,view_kwargs)
        #拦截请求

	#view执行之后，响应之前执行
    def process_response(self,request,response):
        print("response11:",request,response)
        return response #必须返回response
    #如果View中抛出了异常
    def process_exception(self,request,ex):#View中出现异常时执行
        print("exception11:",request,ex)

class MyMiddleAware2(MiddlewareMixin):
    def __init__(self,get_response):#初始化
        super().__init__(get_response)
        print("init22")
	#view处理请求前执行
    def process_request(self,request):
        print(request.path)
        path = settings.EXCLUDE_PATH
        if any((p in request.path for p in path)):
            print("例外")
            return
        if request.session.get("username"):
            print("有身份")
        else:
            msg="请先登录！"
            # request.session['msg'] = msg
            return render(request, 'user/login.html', {"msg": msg})
