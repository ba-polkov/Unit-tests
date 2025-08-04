from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест для add_new_book
    def test_add_new_book_valid_name_length(self):
        """Добавление книги с корректной длинной названия"""
        collector = BooksCollector()
        book_name = "A"*40
        collector.add_new_book(book_name)
        assert book_name in collector.get_book_genre()

    def test_add_new_book_invalid_name_lenght(self):
        """Добваление книги с некорректной длинной названия"""
        collector = BooksCollector()
        long_name = "A"*41
        collector.add_new_book(long_name)
        assert long_name in collector.get_book_genre()

    def test_add_new_book_empty_name_not_add (self):
        """Добавление книги с пустым названием"""
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_set_and_get_book_genre_success(self):
        """Устанавка и получение жанра книги"""
        collector = BooksCollector()
        book_name = "Тестовая книга"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre(book_name) == genre

    def test_get_book_genre_book_without_genree(self):
        """Проверка возврата пустой сроки при добавлении книги без жанра"""
        collector = BooksCollector()
        book_name = "Книга"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre_return_corrrect_list(self):
        """Проверка получения книг с определенным жанром"""
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_new_book("книга 3")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Фантастика")
        collector.set_book_genre("Книга 3", "Ужасы")

        result=collector.get_books_with_specific_genre("Фантастика")

        assert "Книга 1" in result
        assert "Книга 2" in result
        assert "Книга 3" not in result
        assert len(result) == 2

    def test_get_books_for_children_excludes_age_rating_books(self):
        """Проверка отсутствия книг с возростным рейтингом в списке книг для детей"""
        collector = BooksCollector()
        collector.add_new_book ("Книга для детей")
        collector.add_new_book ("Книга ужасов")
        collector.add_new_book ("Книга детектив")

        collector.set_book_genre("Книга для детей", "Детская")
        collector.set_book_genre("Книга ужасов", "Ужасы")
        collector.set_book_genre("Книга детектив", "Детективы")

        children_books = collector.get_books_for_children()

        assert "Книга для детей" in children_books
        assert "Книга ужасов" in children_books
        assert "Книга детектив" in children_books

    def test_get_books_genre_return_dict(self):
        """Проверка что метод возвращает словарь"""
        collector = BooksCollector()
        collector.add_new_book("Тестовая книга")
        books_genre = collector.get_book_genre()
        assert isinstance (books_genre, dict)

    def test_add_and_delete_books_from_favorites():
        """Проверка добавления и удаления книг в Избранное"""
        collector = BooksCollector()
        book_favorites = "Тестовая книга"
        collector.add_new_book(book_favorites)

        collector.add_book_in_favorite(book_favorites)
        assert book_favorites in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(book_favorites)
        assert book_favorites not in collector.add_book_in_favorites()
