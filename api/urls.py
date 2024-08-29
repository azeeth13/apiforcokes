from django.urls import path
from .views import CakeApiView,CakeCreateView,CakeCreateApiView,CakeDelete,CakeUpdate,CakeDestroyandUpdate, UserSignUp,Apiproject
from .views import DeleteAccountView
# from . import views

    



urlpatterns = [
    
    path('cakes/',CakeApiView.as_view(),name='Cakes-api'),
    path('postcakes/',CakeCreateView.as_view(),name='Cake-post'),
    path('cakepostviews/',CakeCreateApiView.as_view(),name='Cake-View'),
    path('cakedelete/<int:pk>/',CakeDelete.as_view(),name="Cake-delete"),
    path('cakeupdate/<int:pk>/',CakeUpdate.as_view(),name="Cake-Update"),
    path('cakedelandupdate/<int:pk>/',CakeDestroyandUpdate.as_view()),
    path('apicake/',Apiproject.as_view()),
    path('userapi',UserSignUp.as_view()),
    path('rest-auth/delete-account/<str:username>/', DeleteAccountView.as_view(), name='delete-account'),
    

]