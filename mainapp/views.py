

# Create your views here.
from re import A
from urllib import response
from django.db.models import query
from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,views
from .serializers import mypostserializers,profileserializers,userserializers,AllPostSerializer,AllbgSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import *
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.





class allnewpost(ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    serializer_class=mypostserializers
    queryset=Post.objects.all().order_by("-id")
    
class ProfileView(views.APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def get(self,request):
        user=request.user
        # query=User.objects.get(username=user.username)
        # serializers=userserializers(query)
        pquery=Profile.objects.get(user=user)
        serializer=profileserializers(pquery)
        
        return Response({"message":" token get successfully ","userdata":serializer.data})
    
    
  
class RegisterView(views.APIView):
    
    def post (self,request, format=None):
        serializers=userserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()

            return Response({"success":"success signup",'data':serializers.data})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
class myallpost(APIView):
    def get(self,request):
        data=Post.objects.all().order_by("-id")
        serializers=AllPostSerializer(data,many=True)
        return Response(serializers.data)

class homeBg(APIView):
    def get(self,request):
        data=Background.objects.all().order_by("-id")[:1]
        serializer=AllbgSerializers(data,many=True)
        return  Response (serializer.data)
    
class UpdateprofileUser(views.APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        user=request.user
        data=request.data
        user_obj=User.objects.get(username=user)
        user_obj.first_name = data['first_name']
        user_obj.last_name = data['last_name']
        user_obj.email = data['email']
        user_obj.save()
        
        return Response({'message':"profile update"})

class UpdateprofileMain(views.APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        try:
            user=request.user
            query=Profile.objects.get(user=user)
            serializers=profileserializers(query,data=request.data, context={'request':request})
            serializers.is_valid()
            serializers.save()
            res_smg={"success":"profile update photo"}
        except:
            res_smg={"error":"eeeeerrrrrrorrrrr"}
            print(serializers.errors)
        return Response(res_smg)
            
            
            

        
            

            

            
            
        
        
        