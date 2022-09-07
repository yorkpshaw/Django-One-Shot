from django.contrib import admin
from todos.models import TodoList


class TodolistAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodolistAdmin)
