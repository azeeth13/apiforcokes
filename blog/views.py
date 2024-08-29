from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import ApiCakes


class CakeListView(ListAPIView):
    queryset=ApiCakes.objects.all()
    model=ApiCakes
    
