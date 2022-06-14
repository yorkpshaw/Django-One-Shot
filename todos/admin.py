from django.contrib import admin
from todos.models import TodoItem, TodoList
# Register your models here.

class TodoItemAdmin(admin.ModelAdmin):
    pass

class TodoListAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem, TodoItemAdmin)