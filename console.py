import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("J.K. Rowling")
author_repository.save(author_1)
author_2 = Author("J.R.R. Tolkein")
author_repository.save(author_2)

book_1 = Book("Harry Potter", author_1.id)
book_2 = Book("Lord of the Rings", author_2.id)
book_repository.save(book_1)
book_repository.save(book_2)