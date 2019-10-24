from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from school_mgmt.serializers import *
from django.views.decorators.csrf import csrf_exempt
from school_mgmt.models import *
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User,UserManager
from rest_framework.authtoken import views as tokenView
from django.db.models import *
import string
from random import randint
import datetime


# 1)User Register Api (url:/api/register/)
@api_view(['POST'])
def user_create(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #2)User Login Api (url:/api/login/) Note: Return Token in response
# @api_view(['POST'])
# def user_login(request):
# 	print request.data
# 	serializer = UserLoginSerializer(data=request.data)
# 	if serializer.is_valid():
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#3) Get All universities API (url: /api/university/list/):
@csrf_exempt
@api_view(['GET'])
def university_list(request): 
	universities = University.objects.all()
	serializer = UniversityListSerializer(universities, many=True)
	print serializer.data
	return Response(serializer.data, status=status.HTTP_200_OK)
   

#4) Create new School of particular logged in user (url:/api/school/add/)
@csrf_exempt
@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def school_create(request):
	if request.user.is_authenticated():
		owner = request.user
		
		creator = request.user
		data = request.data
		data['owner']=owner.id
		data['creator'] = creator.id
		serializer = SchoolSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#5) API to get all schools of logged in user (url:/api/school/list/)
@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_list(request):
    if request.user.is_authenticated():
    	schools = School.objects.filter(creator=request.user)
    	serializer = SchoolListSerializer(schools, many=True)
    	return Response(serializer.data, status=status.HTTP_200_OK)
    else:
    	return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#6) API to get details of particular school of logged in user (url:/api/school/details/{id})
@csrf_exempt
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def school_details(request, pk):
	if request.user.is_authenticated():
		try:
			school = School.objects.get(id=pk, creator=request.user)
		except:
			return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)

		serializer = SchoolListSerializer(school, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#7) API to update particular school of logged in user (url:/api/school/update/{id})
@csrf_exempt
@api_view(['PUT'])
@authentication_classes((TokenAuthentication,))
def school_update(request, pk):
    if request.user.is_authenticated():
	    try:
		    school = School.objects.get(id=pk, creator=request.user)
	    except:
		    return Response({'error': 'school id not found'}, status=status.HTTP_400_BAD_REQUEST)

	    serializer = SchoolListSerializer(school, data=request.data, many=False)

	    if serializer.is_valid():
		    serializer.save()
		    return Response(serializer.data, status=status.HTTP_201_CREATED)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#8) API to delete perticular school of logged in user (url:/api/school/delete/{id})
@csrf_exempt
@api_view(['DELETE'])
@authentication_classes((TokenAuthentication,))
def school_delete(request, pk):
    if request.user.is_authenticated():
	    try:
	    	school = School.objects.get(id=pk,creator=request.user)
	    except:
	    	return Response({'error': 'School id not found'}, status=status.HTTP_400_BAD_REQUEST)
	    school.delete()
	    return Response({'success': 'School deleted successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


#9) Api to get all universities in below format(url: /api/university/list/)
@csrf_exempt
@api_view(['GET'])
def university_list2(request): 
	universities = University.objects.all()
	serializer = UniversityListSerializer2(universities, many=True)
	print serializer.data
	return Response(serializer.data, status=status.HTTP_200_OK)


#10) API to POST student details (url: /api/student/add/):
@csrf_exempt
@api_view(['POST'])
def student_create(request):
	one=str(randint(10**(4-1), (10**4)-1))
	two =str(request.data['date_of_birth'])
	sid=request.data['school']
	sname = list(School.objects.filter(id=sid))
	makeitastring0 = ''.join(map(str,sname))
	four=str(makeitastring0.upper())
	three =str(University.objects.get(school__id=sid))
	five =str(two[5:7])
	six =str(two[0:4])
	finalstr= one+two[8:10]+"-"+three[:3].upper()+four[:3]+"-"+five+six
	add=request.data['address']
	cityname=Address.city 
	fulladdress=Address.objects.all().filter(address__id=add)
	data=request.data
	data['SMARTnumber']=finalstr
	serializer = StudentSmartSerializer(data=data)
	if serializer.is_valid():
		serializer.save()
		return Response({'Smart_number' : finalstr,'Data' : serializer.data }, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#11) API to DELETE university by id (also delete related all the school & student records)(url: /api/university/delete/{id})
@csrf_exempt
@api_view(['DELETE'])
def university_delete(request, pk):
	try:
		university = University.objects.get(id=pk)
	except:
		return Response({'error': 'University id not found'}, status=status.HTTP_400_BAD_REQUEST)
	university.delete()
	return Response({'success': 'University,school,student deleted successfully'}, status=status.HTTP_200_OK)
