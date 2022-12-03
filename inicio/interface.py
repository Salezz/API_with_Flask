from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "booksname": "Lord of the Rings",
        "Author": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "booksname": "Harry Potter",
        "Author": "J.K Howling"

    },
    {
        "id": 3,
        "booksname": "James Clear",
        "Author": "Atomics Acts"
    }

]

# Search(all)
@app.route("/books", methods=["GET"])
def search_books():
    return jsonify(books)
# Search(id)
@app.route("/books/<int:id>", methods=["GET"])
def search_book_by_id(id):
    for book in books:
        if book.get("id") ==  id:
            return jsonify(book)


# Edit
@app.route("/books/<int:id>", methods=["PUT"])
def edit_book_by_id(id):
    altered_book = request.get_json()
    for booktable, book in enumerate(books):
        if book.get("id") == id:
            books[booktable].update(altered_book)
            return jsonify(books[booktable])

# Add book
@app.route("/books", methods=["POST"])
def add_Book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

# Delete
@app.route("/books/<int:id>",methods=["DELETE"])
def delete_book(id):
    for booktable, book in enumerate(books):
        if book.get("id") == id:
            del books[booktable]

    return jsonify(books)

app.run(port=500,host="localhost",debug=True)
