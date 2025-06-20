from flask import Flask, request, jsonify

app = Flask("_main_")


app.config['SECRET_KEY'] = 'this_is_my_secret_key'


@app.route("/api/sort-word", methods=['POST'])
def process_word():
    data = request.get_json()
    word = data["data"]

    letters = [letter for letter in word]
    letters.sort(key=None)

    return jsonify({"word" : letters})

app.run(debug=True)