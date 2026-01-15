# Описание методов тестирования и покрытие методов класса BooksCollector

## Для метода add_new_book
- test_add_new_book_valid_name_length - Проверка добалвения книги с корректным наименованием
- test_add_new_book_invalid_name_lenght - Проверка добавления книги с некорректным наименованием
- test_add_new_book_empty_name_not_add  - Проверка добавления книги с пустым наименованием

## Для метода set_book_genre 
- test_set_book_genre_success - Установка жанра существующей книги 
- test_set_book_genre_nonexistent_book - Установка жанра для несуществующей книги
- test_set_book_genre_invallid_genre - Установка невалидного жанра 

## Для метода get_book_genre
- test_get_book_genre_success - Получение жанра существующей книги
- test_get_book_genre_nonexistent_book - Получение жанра несуществующей книги
- test_get_book_genre_book_without_genree - Возвращение пустой строки при запросе жанров, при добавлении книги без жанра 

## Для метода get_books_with_specific_genre
- test_get_books_with_specific_genre_return_corrrect_list - проверка получения книг с определенным жанром 
- test_get_books_with_specific_genre_no_books_found - получение списка книг по жанру, когда книг нет
- test_get_books_with_specific_genre_invallid_genre- получение списка книг по неизвестному жанру 

## Для метода get_books_for_children
- test_get_books_for_children_excludes_age_rating_books - проверка отсутствия книг с возрастным рейтингом в списке книг для детей
- test_get_books_for_children_no_books - Получение списка книг, все книги с возрастным рейтингом

## Для метода get_books_genre 
- test_get_books_genre_return_dict - проверка, что метод возвращает словарь 
 
## Для метода add_book_in_favorites
- test_add_and_delete_books_from_favorites - проверка добавления, получечния и удаления книги в(из) избранное 
- test_add_book_in_favorites_nonexistent_book - проверка добавления в избранное несуществующей книги

## Для метода delete_book_from_favorites
- test_delete_book_from_favorites_success - успешное удаление книги из избранного 

## Для метода get_list_of_favorites_books
- test_get_list_of_favorites_books_returns_list - проверка получения списка избранных книг 
