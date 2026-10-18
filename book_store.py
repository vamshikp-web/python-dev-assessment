# Book class Definition
class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2026# You can use datetime module to get the current year dynamically
        return current_year - self.publication_year
    def get_summary(self):
        return f"Title:{self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.publication_year}"

#Example Usage:
book1 = Book(title = "The pragmatic programmer.", author = "Andrew Hunt, David Thomas", isbn = "978-0201616224", publication_year = 1999)
print(book1.get_summary())
print(f"Book Age: {book1.get_age()} years")