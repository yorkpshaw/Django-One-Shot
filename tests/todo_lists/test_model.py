from django.test import TestCase
from django.db import models
from random import randint

from todos.models import TodoList


class TodoListModelTests(TestCase):
    def test_name_is_charfield(self):
        name = TodoList.name
        self.assertIsInstance(name.field, models.CharField)

    def test_name_field_has_max_length_100(self):
        name = TodoList.name
        self.assertEqual(100, name.field.max_length)

    def test_name_field_is_not_nullable(self):
        name = TodoList.name
        self.assertFalse(name.field.null)

    def test_name_field_is_not_blankable(self):
        name = TodoList.name
        self.assertFalse(name.field.blank)

    def test_created_on_field_is_datetimefield(self):
        created_on = TodoList.created_on
        self.assertIsInstance(created_on.field, models.DateTimeField)

    def test_created_on_field_is_auto_now_add(self):
        created_on = TodoList.created_on
        self.assertTrue(created_on.field.auto_now_add)

    def test_created_on_field_is_not_nullabel(self):
        created_on = TodoList.created_on
        self.assertFalse(created_on.field.null)

    def test_created_on_field_is_blankable(self):
        created_on = TodoList.created_on
        self.assertTrue(created_on.field.blank)

    def test_str_returns_name(self):
        expected = "*" * randint(1, 100)
        list = TodoList(name=expected)
        self.assertEqual(expected, str(list))
