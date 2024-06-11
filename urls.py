from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views
from django.conf import settings # type: ignore
# from Boutique.settings import MEDIA_ROOT
from django.conf.urls.static import static # type: ignore

app_name="app_tayssir"
urlpatterns = [
    path('', views.home,name="home"),
    path('services/',views.services,name="services")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
