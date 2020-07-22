from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer



class TaskList(generics.ListCreateAPIView):
	queryset = Task.objects.all().order_by('-id')
	serializer_class = TaskSerializer



class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer