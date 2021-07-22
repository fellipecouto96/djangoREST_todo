from .serializers import TodoSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Todo
from rest_framework import status


# Methods GET and POST
class TodoListAndCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Methods GET, PUT, DELETE
class TodoDetailsChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer