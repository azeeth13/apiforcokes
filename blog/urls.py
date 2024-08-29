from django.contrib import admin
from .views import CakeListView
from django.urls import path
urlpatterns = [
    path('',CakeListView.as_view(),name='Cake-List'),
]