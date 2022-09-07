from django.shortcuts import render
from django.views.generic.list import ListView

from todos.models import TodoList


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"
