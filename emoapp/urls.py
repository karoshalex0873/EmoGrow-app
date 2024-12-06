from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from emoapp import views

urlpatterns = [
    path("", views.Getstarted, name="getstarted"),
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("main/", views.Main, name="main"),
    path("notice/", views.notices, name="notice"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
