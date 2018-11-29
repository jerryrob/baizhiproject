from django.urls import path, include, re_path

from emcapp import views
#
urlpatterns = [
    path("emp/",include([
        path("detail/", views.emp_detail,name="empdetail"),
        path("addpage/", views.emp_add_page,name="empaddp"),
        path("add/", views.emp_add,name="empadd"),
        path("uptpage/", views.emp_update_page,name="empuptp"),
        path("update/", views.emp_update,name="empupt"),
        path("delete/", views.emp_delete,name="empdel"),
    ])),
]