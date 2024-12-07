from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from EmoGrow import settings
from emoAdmins import views
from django.conf.urls.static import static

urlpatterns = [
    path("index/", views.admin_site, name="index"),
    path("loginAdmin/", views.adminLogin, name="loginAdmin"),
    path("upload/", views.Upload, name="upload"),
    path("post-question/", views.post_question, name="post_question"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
