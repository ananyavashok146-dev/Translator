from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    text = request.json["text"]

    translated = GoogleTranslator(source='en', target='kn').translate(text)

    return jsonify({"translated": translated})

if __name__ == "__main__":
    app.run(debug=True)