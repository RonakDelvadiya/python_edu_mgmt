from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate, login, logout
from random import randint
import datetime


class StudentSmartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('first_name','last_name','date_of_birth','email','address','school','roll_no') 
   



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_at', 'modified_at')       


class UniversityListSerializer(serializers.ModelSerializer):
     
    count_school = serializers.SerializerMethodField()
    
    class Meta:
        model = University
        fields = ('name','website','is_active','created_at', 'modified_at','count_school')

    def get_count_school(self, obj):
        print obj.id
        return School.objects.filter(discussion_type=obj.id).count()
    
class SchoolUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','university')       
    

        
class UniversityListSerializer2(serializers.ModelSerializer):
     
    school_name = serializers.SerializerMethodField()
    
    class Meta:
        model = University
        fields = ('id','name','school_name')

    def get_school_name(self, obj):
        print obj.id
        return SchoolUniSerializer(School.objects.filter(university__id=obj.id),many=True).data
    

class SchoolListSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = School
        exclude = ('created_at', 'modified_at','owner')



# class StudentListSerializer(serializers.ModelSerializer):
#     # school = serializers.SerializerMethodField()
#     creator = UserSerializer()

#     class Meta:
#         model = Student
        
#     # def get_countschool(self, obj):
#           queryset = 
#     #     school = School.objects.filter(post=obj)
#     #     serializer = CommentSerializer(comments, many=True)
#     #     return serializer.data

