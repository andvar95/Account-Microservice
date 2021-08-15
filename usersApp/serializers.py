from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','username','email','password','phone','address','is_active')
        extra_kwargs = {'password':{
            'write_only':True
        }}

    def create(self,validated_data):
        user = User(
            first_name = validated_data['first_name'],
            username = validated_data['username'],
            email= validated_data['email'],
            phone=validated_data['phone'],
            address=validated_data['address']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def createAdmin(self,validated_data):
        user = self.create(validated_data)
        user.is_superuser = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['password'])
        instance.email = validated_data['email']
        instance.phone = validated_data['phone']
        instance.address = validated_data['address']
        instance.username = validated_data['username']
        instance.save()
        return instance

