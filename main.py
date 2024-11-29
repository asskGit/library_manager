import sys
from library import Library


def main():
    library = Library()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выйти")

        choice = input("\nВаш выбор: ")

        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = int(input("Год издания: "))
            book = library.add_book(title, author, year)
            print(f"Книга добавлена: {book}")

        elif choice == "2":
            book_id = int(input("ID книги: "))
            library.remove_book(book_id)
            print(f"Книга с ID {book_id} удалена.")

        elif choice == "3":
            field = input("Искать по (title, author, year): ")
            query = input("Введите запрос: ")
            results = library.find_books(query, field)
            print(f"Найдено книг: {len(results)}")
            for book in results:
                print(book)

        elif choice == "4":
            books = library.list_books()
            print("Список книг:")
            for book in books:
                print(book)

        elif choice == "5":
            book_id = int(input("ID книги: "))
            status = input("Новый статус (в наличии/выдана): ")
            library.update_status(book_id, status)
            print(f"Статус книги с ID {book_id} обновлен.")

        elif choice == "0":
            print("Выход из программы.")
            sys.exit()

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
