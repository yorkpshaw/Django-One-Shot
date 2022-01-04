from django.test import Client, TestCase
from tests.parsers import PostFormParser
from todos.models import TodoList, TodoItem


class TodoItemCreateViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.list = TodoList.objects.create(name="MyList")

    def setUp(self):
        self.client = Client()
        self.path = f"/todos/items/create/"
        self.response = self.client.get(self.path)
        self.content = self.response.content.decode("utf-8")

    def test_create_view_has_post_form(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue(parser.found)

    def test_create_view_has_task_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("task" in parser.inputs)

    def test_create_view_has_due_date_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("due_date" in parser.inputs)

    def test_create_view_has_is_completed_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("is_completed" in parser.inputs)

    def test_create_view_has_list_field(self):
        parser = PostFormParser()
        parser.feed(self.content);
        self.assertTrue("list" in parser.selects)

    def test_create_post_redirects(self):
        form_data = {"task": "Work!!!", "list": self.list.id}
        response = self.client.post(self.path, form_data)
        self.assertEqual(302, response.status_code)

    def test_create_post_creates_item(self):
        form_data = {"task": "FEED PETS!!!", "list": self.list.id}
        self.client.post(self.path, form_data)
        TodoItem.objects.get(task="FEED PETS!!!")

    def test_create_post_does_not_redirect_for_empty_name(self):
        response = self.client.post(self.path, {"task": ""})
        self.assertEqual(200, response.status_code)
