from django.urls import path, include, re_path

from ajaxapp import views

urlpatterns = [
    path("ajax/",include([
        path("suggest/",views.suggest,name="suggest"),
        path("names/", views.suggestCon,name="getName"),
        path("fileupload/", views.upload,name="upload"),
        path("upload/", views.uploadFile, name="uploadFile"),
    ])),


]