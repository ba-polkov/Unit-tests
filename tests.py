import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
            return BooksCollector()
  
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    # тест для add_new_book
    def test_add_new_book_valid_name_length(self, collector):
        """Добавление книги с корректной длинной названия"""
        book_name = "A"*40
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_invalid_name_lenght(self, collector):
        """Добваление книги с некорректной длинной названия"""
        long_name = "A"*41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_not_add (self, collector):
        """Добавление книги с пустым названием"""
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_set_book_genre_success(self, collector):
        """Устанавка жанра для существующей книги"""
        book_name = "Тестовая книга"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre [book_name] == genre

    def test_set_book_genre_nonexistent_book(self, collector):
        """Установка жанра для несуществующей книги"""
        book_name = "Несуществующая книга"
        genre = "Фантастика"
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.books_genre

    def test_set_book_genre_invallid_genre(self, collector):
        """Установка невалдиного жанра"""
        book_name = "Тестовая книга"
        genre = "Невалидный жанр"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name]== ""

    def test_get_book_genre_success(self, collector):
        """Получение жанра книги"""
        book_name = "Тестовая книга"
        genre = "Детективы"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        result = collector.get_book_genre(book_name)
        assert result == genre

    def get_book_genre_nonxistent_book(self, collector):
        """Получение жанра несуществующей книги"""
        book_name = "Несуществующая книга"
        result = collector.get_book_genre(book_name)
        assert result == None

    def test_get_book_genre_book_without_genree(self, collector):
        """Проверка возврата пустой сроки при добавлении книги без жанра"""
        book_name = "Книга"
        collector.add_new_book(book_name)
        result = collector.get_book_genre(book_name)
        assert result == ""

    def test_get_books_with_specific_genre_return_corrrect_list(self, collector):
        """Проверка получения книг с определенным жанром"""
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

    def test_get_books_with_specific_genre_no_books_found(self, collector):
        """ПОлучение списка книг по жанру, когда книги не найдены"""
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", "Детектив")
        result = collector.get_books_with_specific_genre("Ужасы")

        assert result == []

    def test_get_books_with_specific_genre_invallid_genre(self, collector):
        """ПОлучение списка книг по неизвестному жанру"""
        collector.add_new_book("Тестовая книга")
        collector.set_book_genre("Тестовая книга", "Детектив")
        result = collector.get_books_with_specific_genre("ЛитРПГ")

        assert result == []

    def test_get_books_for_children_excludes_age_rating_books(self, collector):
        """Проверка отсутствия книг с возростным рейтингом в списке книг для детей"""
        collector.add_new_book ("Книга для детей")
        collector.add_new_book ("Книга ужасов")
        collector.add_new_book ("Книга детектив")

        collector.set_book_genre("Книга для детей", "Мультфильмы")
        collector.set_book_genre("Книга ужасов", "Ужасы")
        collector.set_book_genre("Книга детектив", "Детективы")

        children_books = collector.get_books_for_children()

        assert "Книга для детей" in children_books
        assert "Книга ужасов" not in children_books
        assert "Книга детектив" not in children_books

    def test_get_books_for_children_no_books(self, collector):
        """ПОлучение списка книг, все книги с возрастным рейтингом"""
        collector.add_new_book ("Книга ужасов")
        collector.add_new_book ("Книга детектив")
        collector.set_book_genre("Книга ужасов", "Ужасы")
        collector.set_book_genre("Книга детектив", "Детективы")

        result = collector.get_books_for_children()

        assert result == []

    def test_get_books_genre_return_dict(self, collector):
        """Проверка что метод возвращает словарь"""
        collector.add_new_book("Тестовая книга")
        books_genre = collector.get_books_genre()
        assert isinstance (books_genre, dict)

    

    def test_add_books_from_favorites_success(self, collector):
        """Проверка добавления книг в Избранное"""
        book_favorites = "Тестовая книга"
        collector.add_new_book(book_favorites)
        collector.add_book_in_favorites(book_favorites)
        assert book_favorites in collector.favorites

    def test_add_book_in_favorites_nonexistent_book (self, collector):
        """Проверка добавления в избранное несуществующей книги"""
        book_favorites = "Несуществующая книга"
        collector.add_book_in_favorites(book_favorites)
        assert book_favorites not in collector.favorites

    def test_delete_book_from_favorites_success (self, collector):
        """Проверка успешного удаления книги из избранного"""
        book_favorites = "Любимая книга"
        collector.add_new_book(book_favorites)
        collector.add_book_in_favorites(book_favorites)
        collector.delete_book_from_favorites(book_favorites)
        assert book_favorites not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_list(self, collector):
        """Проверка получения списка избранных книг"""
        book1 = "Книга 1"
        book2 = "КНига 2"
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.add_book_in_favorites(book1)
        collector.add_book_in_favorites(book2)

        favorites = collector.get_list_of_favorites_books()
        assert isinstance (favorites, list)
        assert book1 in favorites
        assert book2 in favorites
        assert len(favorites) == 2