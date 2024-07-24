from rest_framework import generics, status, views
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
from .services import generate_text


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class GenerateTextView(views.APIView):
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        generated_text = generate_text(prompt)
        return Response({"data": generated_text}, status=status.HTTP_200_OK)
