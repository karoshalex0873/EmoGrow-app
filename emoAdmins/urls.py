from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from EmoGrow import settings
from emoAdmins import views
from django.conf.urls.static import static

urlpatterns = [
    path("index/", views.admin_site, name="index"),
    path("loginAdmin/", views.adminLogin, name="loginAdmin"),
    path("upload/", views.Upload, name="upload"),
    path("upload/delete/<int:assignment_id>/", views.delete_assigment, name="delete"),
    path("questions/", views.Upload_Questions, name="questions"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
