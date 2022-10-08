from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from MyApi.Throttling import JackRateThrottle
from rest_framework import generics
from rest_framework.throttling import ScopedRateThrottle
# Create your views here.


class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]


class ListTodo(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'


class Details(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifytu'


class CreateToDo(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'


class DeleteTodo(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifytu'