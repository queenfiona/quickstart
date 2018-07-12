from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import GroupSerializer,UserSerializer
from django.shortcuts import render

class UserViewSet(viewsets.ModelViewSet):
	# endpoint to allow user to be edited and viewed
	queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
    serializer_class = GroupSerializer
