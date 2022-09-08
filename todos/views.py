from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from todos.models import TodoList


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from pprint import pprint

        pprint(context)
        return context


class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"
    context_object_name = "detailpage"
