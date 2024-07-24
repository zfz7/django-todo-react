from django.urls import path
from .views import GenerateTextView, TaskListCreate, TaskDetail

urlpatterns = [
    path('generate-text/', GenerateTextView.as_view(), name='generate-text'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
