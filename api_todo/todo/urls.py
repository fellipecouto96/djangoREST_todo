from django.urls import path
from .views import TodoListAndCreate, TodoDetailsChangeAndDelete

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailsChangeAndDelete)
]
