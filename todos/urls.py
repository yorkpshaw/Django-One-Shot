from django.urls import path

from todos.views import (
    TodoItemCreateView,
    TodoItemUpdateView,
    TodoListCreateView,
    TodoListDeleteView,
    TodoListDetailView,
    TodoListListView,
    TodoListUpdateView,
)


urlpatterns = [
    path("", TodoListListView.as_view(), name="todo_list_list"),
    path("<int:pk>/", TodoListDetailView.as_view(), name="todo_list_detail"),
    path("create/", TodoListCreateView.as_view(), name="todo_list_create"),
    path(
        "<int:pk>/edit/",
        TodoListUpdateView.as_view(),
        name="todo_list_update",
    ),
    path(
        "<int:pk>/delete/",
        TodoListDeleteView.as_view(),
        name="todo_list_delete",
    ),
    path(
        "items/create/",
        TodoItemCreateView.as_view(),
        name="todo_item_create",
    ),
    path(
        "items/<int:pk>/edit/",
        TodoItemUpdateView.as_view(),
        name="todo_item_update",
    ),
]
