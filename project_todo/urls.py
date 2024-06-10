from django.contrib import admin
from django.urls import path
from app_todos.views import TodoListView, TodoCreateView, TodoUpdate

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', TodoListView.as_view(), name="todo_list"),
    path('create/', TodoCreateView.as_view(), name="todo_create"),
    path('update/<int:pk>', TodoUpdate.as_view(), name="todo_update")
]
