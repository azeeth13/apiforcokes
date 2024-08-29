from django.db import models
from django.db.models import *
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name_uz=models.CharField(max_length=255,verbose_name='name_uz')
    name_ru=models.CharField(max_length=255,verbose_name='name_ru')
    slug=models.SlugField(unique=True,blank=True) 


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name_uz
    
class ApiCakes(models.Model):
    category_uz=models.ForeignKey(to=Category,on_delete=models.CASCADE,verbose_name='Kategoriya_uz')
    name_uz=models.CharField(max_length=255,verbose_name='name')
    cake_weight=models.IntegerField(verbose_name='Tort-massasi')
    fillings=models.CharField(max_length=250,verbose_name='fillings')
    number_persons=models.IntegerField(verbose_name='odam_soni')
    price=models.IntegerField(verbose_name='tort-narxi')
    small_info=models.TextField(max_length=252,verbose_name='samall-info')
    telephone_number=models.IntegerField(verbose_name='telefon-nomer')
    image=models.ImageField(upload_to='photos/')
    slug=models.SlugField(unique=True,blank=True) 
    




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_uz)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name_uz

    

