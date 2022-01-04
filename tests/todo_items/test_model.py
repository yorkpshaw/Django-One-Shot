from django.test import TestCase
from django.db import models
from random import randint

from todos.models import TodoItem, TodoList


class TodoItemModelTests(TestCase):
    def test_task_field_is_charfield(self):
        task = TodoItem.task
        self.assertIsInstance(task.field, models.CharField)

    def test_task_field_has_max_length_of_100(self):
        task = TodoItem.task
        self.assertEqual(100, task.field.max_length)

    def test_due_date_field_is_datetimefield(self):
        due_date = TodoItem.due_date
        self.assertIsInstance(due_date.field, models.DateTimeField)

    def test_due_date_field_has_auto_now_add_false(self):
        due_date = TodoItem.due_date
        self.assertFalse(due_date.field.auto_now_add)

    def test_due_date_field_is_nullable(self):
        due_date = TodoItem.due_date
        self.assertTrue(due_date.field.null)

    def test_due_date_field_can_be_blank(self):
        due_date = TodoItem.due_date
        self.assertTrue(due_date.field.blank)

    def test_is_completed_field_is_booleanfield(self):
        is_completed = TodoItem.is_completed
        self.assertIsInstance(is_completed.field, models.BooleanField)

    def test_is_completed_field_is_not_null(self):
        is_completed = TodoItem.is_completed
        self.assertFalse(is_completed.field.null)

    def test_is_completed_field_is_not_blank(self):
        is_completed = TodoItem.is_completed
        self.assertFalse(is_completed.field.blank)

    def test_is_completed_field_is_false_by_default(self):
        is_completed = TodoItem.is_completed
        self.assertFalse(is_completed.field.default)

    def test_list_field_is_foreign_key(self):
        list = TodoItem.list
        self.assertIsInstance(list.field, models.ForeignKey)

    def test_list_field_is_related_to_todo_list_model(self):
        list = TodoItem.list
        self.assertEqual(list.field.related_model, TodoList)

    def test_list_field_has_related_name_items(self):
        list = TodoItem.list
        self.assertEqual(list.field.related_query_name(), "items")

    def test_list_field_is_on_delete_cascade(self):
        list = TodoItem.list
        self.assertEqual(list.field.remote_field.on_delete, models.CASCADE)

    def test_str_returns_task(self):
        expected = "*" * randint(1, 100)
        item = TodoItem(task=expected)
        self.assertEqual(expected, str(item))
