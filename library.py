import json
from typing import List, Dict


class Library:
    def __init__(self, storage_file: str = "storage.json"):
        """Инициализация библиотеки и загрузка данных из файла."""
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self) -> List[Dict]:
        """Загрузка данных из JSON-файла."""
        try:
            with open(self.storage_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        """Сохранение данных в JSON-файл."""
        with open(self.storage_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> Dict:
        """Добавление новой книги."""
        new_book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии",
        }
        self.books.append(new_book)
        self.save_books()
        return new_book

    def remove_book(self, book_id: int) -> None:
        """Удаление книги по ID."""
        self.books = [book for book in self.books if book["id"] != book_id]
        self.save_books()

    def find_books(self, query: str, field: str) -> List[Dict]:
        """Поиск книг по полю (title, author, year)."""
        return [book for book in self.books if query.lower() in str(book[field]).lower()]

    def list_books(self) -> List[Dict]:
        """Получение списка всех книг."""
        return self.books

    def update_status(self, book_id: int, status: str) -> None:
        """Обновление статуса книги по ID."""
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                break
        self.save_books()
