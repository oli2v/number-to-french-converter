from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from number_to_french_converter.main import convert_list

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    numbers = data.get("numbers", [])
    translated_numbers = convert_list(numbers)
    return jsonify(translated_numbers)


if __name__ == "__main__":
    app.run(debug=True)
