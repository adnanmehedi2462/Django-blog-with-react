from django.urls import path,include
from .import views 
from .urls import *
from .views import *

# all in one 
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
route=routers.DefaultRouter()
route.register("",allnewpost,basename="allnewpost")
# end allin one


urlpatterns = [
    
    path('mypost/',include(route.urls)),
    path('profile',ProfileView.as_view()),  
    path('login',obtain_auth_token),
    path('registers/',RegisterView.as_view()),
    
    path('updateprofile',UpdateprofileUser.as_view()),
    path('updatemainprofile',UpdateprofileMain.as_view()),
    
    
    path('myallpost',myallpost.as_view()),
    path('homeBg',homeBg.as_view()),
    
    
    
    
]
