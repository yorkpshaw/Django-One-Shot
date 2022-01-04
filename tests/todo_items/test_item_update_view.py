from django.test import Client, TestCase
from tests.parsers import PostFormParser
from todos.models import TodoList, TodoItem


class TodoItemUpdateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.list = TodoList.objects.create(name="MyList")

    def setUp(self):
        self.item = TodoItem.objects.create(task="Do it", list=self.list)
        self.client = Client()
        self.path = f"/todos/items/{self.item.id}/edit/"
        self.response = self.client.get(self.path)
        self.content = self.response.content.decode("utf-8")

    def test_update_view_has_post_form(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue(parser.found)

    def test_update_view_has_task_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertIn("task", parser.inputs)

    def test_update_view_has_task_in_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertEqual("Do it", parser.inputs["task"]["value"])

    def test_update_view_has_due_date_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertIn("due_date", parser.inputs)

    def test_update_view_has_is_completed_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertIn("is_completed", parser.inputs)

    def test_update_view_has_is_completed_field_is_not_checked(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertNotIn("checked", parser.inputs["is_completed"])

    def test_update_view_has_list_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("list" in parser.selects)

    def test_update_post_redirects(self):
        form_data = {"task": "Work!!!", "list": self.list.id}
        response = self.client.post(self.path, form_data)
        self.assertEqual(302, response.status_code)

    def test_update_post_updates_item(self):
        form_data = {"task": "FEED PETS!!!", "list": self.list.id}
        self.client.post(self.path, form_data)
        TodoItem.objects.get(task="FEED PETS!!!")

    def test_update_post_does_not_redirect_for_empty_name(self):
        response = self.client.post(self.path, {"task": ""})
        self.assertEqual(200, response.status_code)
