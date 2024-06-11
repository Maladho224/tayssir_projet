from django.contrib import admin # type: ignore
from .models import *

# Register your models here.
class P(admin.ModelAdmin):
    list_display=('title','num','email','fichier','date_create')
class S(admin.ModelAdmin):
    list_display=('auteur','contact','email_auteur','conseil','photo')
admin.site.register(Professeurs,P)
admin.site.register(Services,S)
admin.site.site_title="Tayssir"
admin.site.site_header="Espace d'administration de Tayssir"