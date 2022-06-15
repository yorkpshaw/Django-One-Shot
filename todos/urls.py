from venv import create
from django.urls import path

from todos.views import (
    show_todo_lists,
    show_todo_list,
    create_todo_list,
    update_todo_list,
    delete_todo_list,
    create_todo_item,
    update_todo_item
)


urlpatterns = [
    path("", show_todo_lists, name="todo_list_list"),
    path("<int:pk>/", show_todo_list, name="todo_list_detail"),
    path("create/", create_todo_list, name="todo_list_create"),
    path(
        "<int:pk>/edit/",
        update_todo_list,
        name="todo_list_update",
    ),
    path(
        "<int:pk>/delete/",
        delete_todo_list,
        name="todo_list_delete",
    ),
    path(
        "items/create/",
        create_todo_item,
        name="todo_item_create",
    ),
    path(
        "items/<int:pk>/edit/",
        update_todo_item,
        name="todo_item_update",
    ),
]
