from .models import *
from rest_framework import serializers


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'singer', 'title', 'duration']


class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'city']


