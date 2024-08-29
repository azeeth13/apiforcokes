from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from blog.models import ApiCakes,Category
from .serializer import CakeSer,AllCakesSer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from allauth.account.views import SignupView
from rest_framework.authtoken.models import Token
# from rest_auth.registration.views import RegisterView


# class CustomRegisterView(RegisterView):
#     def get_response_data(self, user):
#         token, created = Token.objects.get_or_create(user=user)
#         return {
#             'user_id': user.pk,
#             'email': user.email,
#             'token': token.key
#         }


class CustomSignupView(SignupView):
    def form_valid(self, form):
        user = form.save(self.request)
        Token.objects.get_or_create(user=user)
        return super().form_valid(form)







class DeleteAccountView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, username, *args, **kwargs):
        try:
            user = User.objects.get(username=username)
            user_data = {
                "username": user.username,
                "email": user.email,
                'password':user.password,
                "date_joined": user.date_joined,
            }
            return Response(user_data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Username not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, username, *args, **kwargs):
        b = User.objects.filter(username=username)
        if b.exists():
            a = User.objects.get(username=username)
            a.delete()
            return Response({"detail": "User account deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)



class UserSignUp(APIView):
    def get(self,request):
        user=User.objects.all()
        return Response({'user':user})
    

    def post(self,request):
        username=request.data['username']
        email=request.data['email']
        password1=request.data['password1']
        password2=request.data['password2']
        if password1==password2:
            new_user=User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
        return Response({'user':model_to_dict(new_user)})
    
class Apiproject(APIView):
    def get(self,request):
        cakes=ApiCakes.objects.all().values()
        return Response({'project':cakes})
    
class CakeApiView(ListAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer


class CakeCreateView(CreateAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer


class CakeCreateApiView(ListCreateAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer

class CakeDelete(RetrieveDestroyAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer

class CakeUpdate(RetrieveUpdateAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer

class CakeDestroyandUpdate(RetrieveUpdateDestroyAPIView):
    queryset=ApiCakes.objects.all()
    serializer_class=AllCakesSer




    