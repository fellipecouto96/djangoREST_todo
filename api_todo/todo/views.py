from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets


# Methods GET, PUT, DELETE and POST
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
