from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from emoapp import views

urlpatterns = [
    path("", views.Getstarted, name="getstarted"),
    path("about", views.About, name="about"),
    path("register/", views.Register, name="register"),
    path("contact/", views.Contact, name="contact"),
    path("price/", views.Pricing, name="price"),
    path("login/", views.Login, name="login"),
    path("show/", views.show_assignment, name="show"),
    path("main/", views.Main, name="main"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
