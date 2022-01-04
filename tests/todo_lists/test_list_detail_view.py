from django.test import Client, TestCase
from tests.parsers import AnchorSearchParser
from todos.models import TodoList, TodoItem


class TodoListDetailViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.lists = [
            TodoList.objects.create(name="Work"),
            TodoList.objects.create(name="Home"),
            TodoList.objects.create(name="Pets"),
        ]

    def setUp(self):
        self.client = Client()
        self.response = self.client.get(f"/todos/{self.lists[0].id}/")
        self.content = self.response.content.decode("utf-8")

    def test_200_for_known_id(self):
        self.assertEqual(200, self.response.status_code)

    def test_404_for_unknown_id(self):
        max_id = self.lists[-1].id
        response = self.client.get(f"/todos/{max_id + 1}/")
        self.assertEqual(404, response.status_code)

    def test_detail_page_has_delete_link(self):
        id = self.lists[0].id
        parser = AnchorSearchParser(f"/todos/{id}/delete/")
        parser.feed(self.content)
        self.assertTrue(parser.found, "Did not find a delete link")

    def test_detail_page_has_edit_link(self):
        id = self.lists[0].id
        parser = AnchorSearchParser(f"/todos/{id}/edit/")
        parser.feed(self.content)
        self.assertTrue(parser.found, "Did not find an edit link")

    def test_detail_page_for_list_with_todo_items(self):
        items = [
            TodoItem.objects.create(
                task=f"Task {i}", is_completed=i % 2 == 0, list=self.lists[0]
            )
            for i in range(5)
        ]
        self.setUp()
        for i, item in enumerate(items):
            with self.subTest(i=i):
                path = f"/todos/items/{item.id}/edit/"
                parser = AnchorSearchParser(path)
                parser.feed(self.content)
                self.assertTrue(
                    parser.found, "Did not find edit link for TodoItem"
                )
