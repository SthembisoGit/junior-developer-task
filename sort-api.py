from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this_is_my_secret_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/sort-word", methods=['POST'])
def process_word():
    data = request.get_json()
    word = data["data"]

    letters = [letter for letter in word]
    letters.sort()

    return jsonify({"word": letters})

if __name__ == "__main__":
    app.run(debug=True)