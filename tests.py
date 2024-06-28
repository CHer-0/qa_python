import pytest
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

    @staticmethod #Создаем и заполняем объект класса BooksCollector книгами
    def coll_fill(books):
        c = BooksCollector()
        for name, genre in books.items():
            # создадем запись о книге
            c.add_new_book(name)
            # Устанавливаем ей жанр
            c.set_book_genre(name, genre)
        return c
    @pytest.mark.parametrize('len_name', [1, 40])
    def test_add_new_book_add_extremal_len_name(self, len_name):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        name = 'a' * len_name
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('len_name', [0, 41])
    def test_add_new_book_add_over_extremal_len_name(self, len_name):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        name = 'a' * len_name
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_genre_not_empty(self):
        collector = BooksCollector()
        assert len(collector.genre) > 0

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Комедии'], ['Что делать, если ваш кот хочет вас убить', 'Комедии']])
    def test_set_book_genre_set_genre_in_list(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector с принятыми параметрами
        books = {name: genre}
        collector = self.coll_fill(books)

        assert len(collector.get_books_genre()) == 1 and collector.books_genre[name] == collector.genre[-1]

    @pytest.mark.parametrize('name, genre', [['Гордость и предубеждение и зомби', 'Роман'], ['Что делать, если ваш кот хочет вас убить', 'Поэма']])
    def test_set_book_genre_set_genre_not_in_list(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector с жанром не из перечня
        books = {name: genre}
        collector = self.coll_fill(books)

        assert collector.books_genre[name] != genre

    def test_get_book_genre_exist_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # создадем запись о книге
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        # Устанавливаем жанр из перечня
        genre = 'Комедии'
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_not_exist_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # создадем запись о книге
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        # Устанавливаем жанр из перечня
        genre = 'Комедии'
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre('Wrong name') != genre

    def test_get_books_with_specific_genre_two_exist_book_genre(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами с жанром Комедии
        books = {'Гордость и предубеждение и зомби': 'Комедии', 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)

        assert len(collector.get_books_with_specific_genre('Комедии')) == 2

    def test_get_books_with_specific_genre_not_book_genre(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами с жанром не из перечня Роман
        books = {'Гордость и предубеждение и зомби': 'Роман', 'Что делать, если ваш кот хочет вас убить': 'Роман'}
        collector = self.coll_fill(books)

        assert len(collector.get_books_with_specific_genre('Роман')) == 0

    def test_get_books_genre_return_dict(self):
        # создаем экземпляр (объект) класса BooksCollector с книгой
        collector = BooksCollector()
        # создадем запись о книге
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        # Устанавливаем жанр из перечня
        genre = 'Комедии'
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == {name: genre}

    def test_get_books_for_children_two_books_for_children(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами с жанром не из перечня для взрослых
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)

        assert len(collector.get_books_for_children()) == 2

    def test_get_books_for_children_two_books_not_for_children(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами с жанром из перечня для взрослых
        books = {'Гордость и предубеждение и зомби': 'Ужасы',
                 'Что делать, если ваш кот хочет вас убить': 'Детективы'}
        collector = self.coll_fill(books)

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_two_exist_books(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)
        # добавляем книги в перечень избранных
        for book in books:
            collector.add_book_in_favorites(book)

        assert len(collector.favorites) == 2

    def test_add_book_in_favorites_two_not_exist_books(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)
        not_exist_books = ['Идиот',
                 'Что делать?']
        # пытаемся добавить книги не из коллекции в перечень избранных
        for book in not_exist_books:
            collector.add_book_in_favorites(book)

        assert len(collector.favorites) == 0

    def test_delete_book_from_favoritess_two_exist_books(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)
        # добавляем книги в перечень избранных
        for book in books:
            collector.add_book_in_favorites(book)
        # количество избранных книг после добавления
        count_favorites_before_del = len(collector.favorites)
        # удаляем добавленные книги из избранных
        for book in books:
            collector.delete_book_from_favorites(book)
        # количество избранных книг после удаления
        count_favorites_after_del = len(collector.favorites)

        assert count_favorites_before_del == 2 and count_favorites_after_del == 0

    def test_delete_book_from_favoritess_two_not_exist_books(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)
        # добавляем книги в перечень избранных
        for book in books:
            collector.add_book_in_favorites(book)
        count_favorites_before_del = len(collector.favorites)
        # пытаемся удалить книги из избранных, которых нет в перечне
        not_exist_books = ['Идиот',
                           'Что делать?']
        for book in not_exist_books:
            collector.delete_book_from_favorites(book)
        count_favorites_after_del = len(collector.favorites)

        assert count_favorites_before_del == count_favorites_after_del

    def test_get_list_of_favorites_books_return_list(self):
        # создаем экземпляр (объект) класса BooksCollector с 2 книгами
        books = {'Гордость и предубеждение и зомби': 'Фантастика',
                 'Что делать, если ваш кот хочет вас убить': 'Комедии'}
        collector = self.coll_fill(books)
        # добавляем книги в перечень избранных
        expected_list = []
        for book in books:
            collector.add_book_in_favorites(book)
            # создаем список избранных книг, который ожидается при выполнении метода
            expected_list.append(book)

        assert collector.get_list_of_favorites_books() == expected_list
