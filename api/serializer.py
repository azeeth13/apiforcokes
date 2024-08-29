from rest_framework import serializers
from blog.models import *


class CakeSer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    
class AllCakesSer(serializers.ModelSerializer):
    class Meta:
        model=ApiCakes
        fields='__all__'
