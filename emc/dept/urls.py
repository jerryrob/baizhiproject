from django.urls import path, include, re_path

from dept import views
#
urlpatterns = [
    path("dept/",include([
        path("query/", views.dept_list,name="deptquery"),
        path("addpage/", views.add_page,name="deptaddp"),
        path("add/", views.add,name="deptadd"),
        path("uptpage/", views.update_page,name="deptuptp"),
        path("update/", views.update,name="deptupt"),
        path("delete/", views.del_dept,name="deptdel"),
    ])),
]