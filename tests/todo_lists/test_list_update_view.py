from django.test import Client, TestCase
from tests.parsers import PostFormParser
from todos.models import TodoList


class TodoListUpdateViewTests(TestCase):
    def setUp(self):
        self.list = TodoList.objects.create(name="Pets")
        self.client = Client()
        self.path = f"/todos/{self.list.id}/edit/"
        self.response = self.client.get(self.path)
        self.content = self.response.content.decode("utf-8")

    def test_update_view_has_post_form(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue(parser.found)

    def test_update_view_has_name_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("name" in parser.inputs)

    def test_update_view_has_name_in_field_value(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertEqual("Pets", parser.inputs.get("name").get("value"))

    def test_update_post_redirects(self):
        response = self.client.post(self.path, {"name": "Work!!!"})
        self.assertEqual(302, response.status_code)

    def test_update_post_updates_item(self):
        self.client.post(self.path, {"name": "Work!!!!"})
        TodoList.objects.get(name="Work!!!!")

    def test_update_post_does_not_redirect_for_empty_name(self):
        response = self.client.post(self.path, {"name": ""})
        self.assertEqual(200, response.status_code)
