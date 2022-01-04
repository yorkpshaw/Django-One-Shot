from django.test import Client, TestCase
from tests.parsers import PostFormParser
from todos.models import TodoList, TodoItem


class TodoListDeleteViewTests(TestCase):
    def setUp(self):
        self.list = TodoList.objects.create(name="Work")
        self.items = [
            TodoItem.objects.create(task="Task 1", list=self.list),
            TodoItem.objects.create(task="Task 2", list=self.list),
            TodoItem.objects.create(task="Task 3", list=self.list),
        ]
        self.client = Client()
        self.path = f"/todos/{self.list.id}/delete/"

    def test_get_delete_view_has_post_form(self):
        response = self.client.get(self.path)
        content = response.content.decode("utf-8")
        parser = PostFormParser()
        parser.feed(content)
        self.assertTrue(parser.found, "Did not find a post form on delete page")

    def test_get_delete_view_is_200_for_known_id(self):
        response = self.client.get(self.path)
        self.assertEqual(200, response.status_code)

    def test_get_delete_view_is_404_for_unknown_id(self):
        response = self.client.get("/todos/0/delete/")
        self.assertEqual(404, response.status_code)

    def test_post_delete_is_302(self):
        response = self.client.post(self.path)
        self.assertEqual(302, response.status_code)

    def test_post_delete_removes_list_from_database(self):
        self.client.post(self.path)
        with self.assertRaises(TodoList.DoesNotExist):
            TodoList.objects.get(id=self.list.id)

    def test_post_delete_removes_list_items_from_database(self):
        self.client.post(self.path)
        self.assertEqual(0, len(TodoItem.objects.all()))
