import unittest
from library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("test_storage.json")
        self.library.books = []

    def tearDown(self):
        self.library.save_books()

    def test_add_book(self):
        book = self.library.add_book("Test Title", "Test Author", 2024)
        self.assertEqual(book["title"], "Test Title")

    def test_remove_book(self):
        book = self.library.add_book("Test Title", "Test Author", 2024)
        self.library.remove_book(book["id"])
        self.assertEqual(len(self.library.books), 0)

    def test_find_books(self):
        self.library.add_book("Test Title", "Test Author", 2024)
        results = self.library.find_books("Test", "title")
        self.assertEqual(len(results), 1)

    def test_update_status(self):
        book = self.library.add_book("Test Title", "Test Author", 2024)
        self.library.update_status(book["id"], "выдана")
        self.assertEqual(self.library.books[0]["status"], "выдана")


if __name__ == "__main__":
    unittest.main()
