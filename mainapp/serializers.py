


from importlib.metadata import files
from pyexpat import model
from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User=get_user_model()
class userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password","first_name","last_name","email")
        extra_kwargs={'password':{'write_only':True,'required':True}}
        
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        return user
    
            
     

class profileserializers(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"
        read_only_fiels=['user']
        extra_kwargs = {'user': {'required': False}}
        
    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

    def to_representation(self, instance):
        response= super().to_representation(instance)
        response['user']=userserializers(instance.user).data
        return response
        
        
        
        
class mypostserializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"
        read_only_fiels=['author']
        depth=1
    def to_representation(self, instance):
        response= super().to_representation(instance)
        response['author']=profileserializers(instance.author.profile).data
        return response
    def validate(self, obj):  #ja login ase react e se kuno kicho post korle auto sai select hobe
        obj['author']=self.context['request'].user
        return obj
        
        
class AllPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fiels=['author']
        depth=1

    def to_representation(self, instance):
        response= super().to_representation(instance)
        response['author']=profileserializers(instance.author.profile).data
        return response


class AllbgSerializers(ModelSerializer):
    class Meta:
        model=Background
        fields="__all__"
        
