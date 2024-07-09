from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/data")
def get_data():
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"},
        ]
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
