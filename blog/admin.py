from django.contrib import admin
from .models import *


class ArticleAdmins(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_uz',)}



@admin.register(Category)
class CategAdmin(ArticleAdmins):
    list_display=('name_uz','name_ru','id',)


@admin.register(ApiCakes)
class ApiCakes(ArticleAdmins):
    list_display=('category_uz','cake_weight','fillings','number_persons','price','small_info','telephone_number','image','id',)



