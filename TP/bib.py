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

    def __str__(self):
        return f'this is a book {self.title}'
    
    def __repr__(self):
        return f'this is a book {self.title}'
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    class MyLibrary:
        def __init__(self):
            self._library = []

    def add_to_library(book):
        library.append(book)
    
    def remove_from_library(book):
        library.remove(book)
    
    def update_book(book):
        pass

library = []

if __name__ == '__main__':
    b = Book('foundation', 'Isaac', '/path/to/book.e')
    print(b.author)
    b.author = 'Asimov'
    # read input from user to handle library collection
    # create 
    # read
    # update
    # delete