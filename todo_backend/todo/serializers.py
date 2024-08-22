from rest_framework import serializers
from .models import Task, TranslatedTask


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'description']


class TranslatedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedTask
        fields = ['id', 'title', 'translatedTitle', 'completed', 'description']
