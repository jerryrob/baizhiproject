from django.urls import path, include, re_path

from userapp import views

urlpatterns = [
    path("register/",include([
        path("page/",views.register_page,name="registerp"),
        path("register/", views.register,name="register"),
        path("checkUsername/", views.check_username,name="checkName"),
    ])),
    path("login/", include([
        path("page/", views.login_page,name="loginp"),
        path("login/", views.login,name='login'),
        path("atest/", views.ajaxPage, name='ajaxtest'),
        path("btest/", views.ajax_test1, name='test_1'),
        path("ctest/", views.ajax_test2, name='test_2'),
        path("checkCode/", views.check_code,name="checkCode"),
        path("index/", views.index,name="index"),
    ])),
    path("cap/", include([
        path("getcap/", views.generate_captcha, name="code"),
    ])),
    path("json/", include([
        path("test1/", views.json_page, name="page"),
        path("test2/", views.json_test1, name="jsonta"),
    ])),
    path("ajax/",include([
        path("test1/",views.ajax_page1,name="ajax1"),
        path("test2/",views.ajax_page2,name="ajax2"),
    ])),

]