from django.urls import path

from todos.views import (
    TodoListView,
    TodoDetailView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list_list"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_list_detail"),
]
