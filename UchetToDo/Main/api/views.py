from django.shortcuts import render
from Task.models import *
from .serializers import *
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from rest_framework import status








class AllTasks(APIView):
    def get(request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)


    def post(self, request, format=None):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)



class TaskDetail(APIView):
    def get(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return HttpResponse(status=404)

        serializer = TaskSerializers(task)
        return JsonResponse(serializer.data)


    def put(self, request, id, format=None):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return HttpResponse(status=404)
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)


    def delete(self, request, id, format=None):
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponse(status=204)



class TaskExecute(APIView):
    def post(self, request, id, format=None):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return HttpResponse(status=404)
        task.isDone = True
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)



class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully added a new user'
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)



class UpdateUser(generics.UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    model = User
    def get_object(self, queryset=None):
        return self.request.user


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
