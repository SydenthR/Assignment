# Book CRUD API using Flask
# This follows the same structure as the Drink API example, but for books

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "book_name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "book_name": request.json.get("book_name"),
        "author": request.json.get("author"),
        "publisher": request.json.get("publisher")
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            book["book_name"] = request.json.get("book_name", book["book_name"])
            book["author"] = request.json.get("author", book["author"])
            book["publisher"] = request.json.get("publisher", book["publisher"])
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)