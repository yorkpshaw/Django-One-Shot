from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from todos.models import TodoItem, TodoList


class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_lists/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todo_lists/detail.html"


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todo_lists/create.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todo_lists/update.html"
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todo_lists/delete.html"
    success_url = reverse_lazy("todo_list_list")


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo_items/create.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.list.id])


class TodoItemUpdateView(UpdateView):
    model = TodoItem
    template_name = "todo_items/update.html"
    fields = ["task", "due_date", "is_completed", "list"]

    def get_success_url(self):
        return reverse_lazy("todo_list_detail", args=[self.object.list.id])
