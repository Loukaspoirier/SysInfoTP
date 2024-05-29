import jsonpickle

class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if len(value) > 3:
            self._author = value
        else:
            raise ValueError("Author name must be longer than 3 characters.")

    def __str__(self):
        return f'This is a book titled "{self.title}" by {self.author}.'

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author})'

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


class MyLibrary:
    def __init__(self):
        self._library = []
        self.__load()

    def add_to_library(self, book):
        self._library.append(book)
        print(f'Added book: {book}')

    def remove_from_library(self, book):
        if book in self._library:
            self._library.remove(book)
            print(f'Removed book: {book}')
        else:
            print('Book not found in library.')

    def update_book(self, old_book, new_book):
        if old_book in self._library:
            index = self._library.index(old_book)
            self._library[index] = new_book
            print(f'Updated book: {old_book} to {new_book}')
        else:
            print('Book not found in library.')

    def display_library(self):
        for book in self._library:
            print(book)

    def __load(self):
        with open('save.json', 'r') as f:
            strjson = f.read()
            self.__library = jsonpickle.decode(strjson)._MyLibrary__library

    def save(self):
        with open('save.json', 'w') as f:
            f.write(jsonpickle.encode(self))


def handle_create(library):
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    content = input('Enter book content (path or description): ')
    book = Book(title, author, content)
    library.add_to_library(book)


def handle_read(library):
    library.display_library()


def handle_update(library):
    title = input('Enter the title of the book to update: ')
    author = input('Enter the author of the book to update: ')
    old_book = Book(title, author, '')
    
    new_title = input('Enter new book title: ')
    new_author = input('Enter new book author: ')
    new_content = input('Enter new book content (path or description): ')
    new_book = Book(new_title, new_author, new_content)
    
    library.update_book(old_book, new_book)


def handle_delete(library):
    title = input('Enter the title of the book to delete: ')
    author = input('Enter the author of the book to delete: ')
    book = Book(title, author, '')
    library.remove_from_library(book)


if __name__ == '__main__':
    library = MyLibrary()
    action = ''
    while action != 'q':
        action = input('Choose action: (c)reate, (r)ead, (u)pdate, (d)elete, (q)uit: ').strip().lower()
        if action == 'c':
            handle_create(library)
        elif action == 'r':
            handle_read(library)
        elif action == 'u':
            handle_update(library)
        elif action == 'd':
            handle_delete(library)
        elif action == 'q':
            print('Exiting the program.')
        else:
            print('Invalid action. Please choose again.')
