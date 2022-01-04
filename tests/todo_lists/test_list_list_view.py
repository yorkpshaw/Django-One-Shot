from django.test import Client, TestCase
from tests.parsers import AnchorSearchParser
from todos.models import TodoList


class TodoListListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.lists = [
            TodoList.objects.create(name="Work"),
            TodoList.objects.create(name="Home"),
            TodoList.objects.create(name="Pets"),
        ]

    def setUp(self):
        self.client = Client()
        self.response = self.client.get("/todos/")
        self.content = self.response.content.decode("utf-8")

    def test_todo_list_list_returns_200(self):
        self.assertEqual(200, self.response.status_code)

    def test_todo_list_list_has_detail_links(self):
        for i, list in enumerate(self.lists):
            with self.subTest(i=i):
                parser = AnchorSearchParser(f"/todos/{list.id}/")
                parser.feed(self.content)
                self.assertTrue(parser.found, "Did not find a detail link")

    def test_todo_list_list_has_list_names(self):
        for i, list in enumerate(self.lists):
            name = list.name
            with self.subTest(i=i):
                self.assertRegex(self.content, f"""\\b{name}\\b""")

    def test_todo_list_list_has_link_to_create_list(self):
        parser = AnchorSearchParser("/todos/create/")
        parser.feed(self.content)
        self.assertTrue(parser.found, "Did not find a create list link")

    def test_todo_list_list_has_link_to_create_item(self):
        parser = AnchorSearchParser("/todos/items/create/")
        parser.feed(self.content)
        self.assertTrue(parser.found, "Did not find a create item link")
