import os

FILENAME = "library.txt"


def add_book():
    title = input("Введіть назву книги: ").strip()
    author = input("Введіть автора книги: ").strip()
    with open(FILENAME, "a", encoding="utf-8") as file:
        file.write(f"{title};{author}\n")
    print("✅ Книгу додано!")


def view_books():
    if not os.path.exists(FILENAME):
        print("Бібліотека порожня.")
        return
    with open(FILENAME, "r", encoding="utf-8") as file:
        books = file.readlines()
    if not books:
        print("Бібліотека порожня.")
    else:
        print("\n📚 Усі книги:")
        for i, line in enumerate(books, start=1):
            title, author = line.strip().split(";")
            print(f"{i}. {title} — {author}")


def search_by_author():
    author_search = input("Введіть ім'я автора для пошуку: ").strip().lower()
    found = False
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                title, author = line.strip().split(";")
                if author_search in author.lower():
                    print(f"🔎 Знайдено: {title} — {author}")
                    found = True
    if not found:
        print("❌ Книг цього автора не знайдено.")


def delete_book():
    title_delete = input("Введіть назву книги для видалення: ").strip().lower()
    if not os.path.exists(FILENAME):
        print("Файл бібліотеки порожній.")
        return
    with open(FILENAME, "r", encoding="utf-8") as file:
        books = file.readlines()
    new_books = []
    deleted = False
    for line in books:
        title, author = line.strip().split(";")
        if title.lower() == title_delete:
            deleted = True
        else:
            new_books.append(line)
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.writelines(new_books)
    if deleted:
        print("🗑 Книгу видалено!")
    else:
        print("❌ Книгу не знайдено.")


def main():
    while True:
        print("\n===== Бібліотека =====")
        print("1. Додати нову книгу")
        print("2. Переглянути всі книги")
        print("3. Пошук книги за автором")
        print("4. Видалити книгу")
        print("5. Вихід")
        choice = input("Оберіть дію (1-5): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_by_author()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("👋 Вихід з програми.")
            break
        else:
            print("❌ Неправильний вибір!")


if __name__ == "__main__":
    main()
