from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.book_title, book.author_id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book




def select_all():

    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row["id"])
        book = Book(row["title"], author, row["id"])
        books.append(book)
    
    return books

delete