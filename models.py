from django.db import models # type: ignore

# Create your models here.
class Professeurs(models.Model):
    title= models.CharField(max_length=50,default="")
    num= models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default='')
    fichier=models.FileField(upload_to='PDF', max_length=100)
    date_create=models.DateField( auto_now=True)
    
    def __str__(self):
        return self.title
class Services(models.Model):
    auteur=models.CharField(default="",max_length=50)
    contact=models.IntegerField(default="")
    email_auteur=models.EmailField( default="",max_length=254)
    title_services=models.CharField(default="",max_length=50)
    conseil=models.TextField(default="")
    photo=models.ImageField(upload_to="image")

    def __str__(self):
        return self.title_services

    

