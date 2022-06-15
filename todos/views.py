from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from todos.forms import TodoItemForm, TodoListForm

from todos.models import TodoItem, TodoList


# class TodoListListView(ListView):
#     model = TodoList
#     template_name = "todo_lists/list.html"


def show_todo_lists(request):
    todolists = TodoList.objects.all()
    return render(request, "todo_lists/list.html", {"todolist_list": todolists})


# class TodoListDetailView(DetailView):
#     model = TodoList
#     template_name = "todo_lists/detail.html"


def show_todo_list(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    return render(request, "todo_lists/detail.html", {"todolist": todolist})


# class TodoListCreateView(CreateView):
#     model = TodoList
#     template_name = "todo_lists/create.html"
#     fields = ["name"]

#     def get_success_url(self):
#         return reverse_lazy("todo_list_detail", args=[self.object.id])


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", todolist.pk)
    else:
        form = TodoListForm()
    return render(request, "todo_lists/create.html", {"form": form})


# class TodoListUpdateView(UpdateView):
#     model = TodoList
#     template_name = "todo_lists/update.html"
#     fields = ["name"]

#     def get_success_url(self):
#         return reverse_lazy("todo_list_detail", args=[self.object.id])


def update_todo_list(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", todolist.pk)
    else:
        todolist = get_object_or_404(TodoList, pk=pk)
        form = TodoListForm(instance=todolist)
    return render(request, "todo_lists/create.html", {"form": form})


# class TodoListDeleteView(DeleteView):
#     model = TodoList
#     template_name = "todo_lists/delete.html"
#     success_url = reverse_lazy("todo_list_list")


def delete_todo_list(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list_list")
    return render(request, "todo_lists/delete.html")


# class TodoItemCreateView(CreateView):
#     model = TodoItem
#     template_name = "todo_items/create.html"
#     fields = ["task", "due_date", "is_completed", "list"]

#     def get_success_url(self):
#         return reverse_lazy("todo_list_detail", args=[self.object.list.id])


def create_todo_item(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todoitem = form.save()
            return redirect("todo_list_detail", todoitem.list.id)
    else:
        form = TodoItemForm()
    return render(request, "todo_items/create.html", {"form": form})


# class TodoItemUpdateView(UpdateView):
#     model = TodoItem
#     template_name = "todo_items/update.html"
#     fields = ["task", "due_date", "is_completed", "list"]

#     def get_success_url(self):
#         return reverse_lazy("todo_list_detail", args=[self.object.list.id])


def update_todo_item(request, pk):
    todoitem = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem)
        if form.is_valid():
            form.save()
            return redirect("todo_list_detail", todoitem.list.id)
    else:
        form = TodoItemForm(instance=todoitem)
    return render(request, "todo_items/update.html", {"form": form})
