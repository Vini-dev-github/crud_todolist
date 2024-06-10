from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    #template_name = 'todos/todo_list.html'

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")
