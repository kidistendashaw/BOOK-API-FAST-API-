from fastapi import FastAPI
from typing import Optional


app = FastAPI()

# ---- Fake Database ----
books =[
    {"id": 1, "title": "Atomic Habits", "author": "James Clear"},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho"},
]

@app.get("/books")
def get_books():
    return {"books": books}
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}
@app.post("/books")
def create_book(title: str, author: str):
    new_book = {"id": new_id, "title": title, "author": author}
    books.append(new_book)
    return {"message": "Book created", "book": new_book}
@app.put("/books/{book_id}")
def update_book(book_id: int, title: Optional[str] = None, author: Optional[str] = None):
    for book in books:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            return {"message": "Book updated", "book": book}
    return {"error": "Book not found"}
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}



