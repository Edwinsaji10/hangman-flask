from flask import Flask, jsonify, render_template, send_from_directory
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('static', 'style.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory('static', 'script.js')

@app.route('/get-word')
def get_word():
    with open("words.txt", "r") as f:
        words = [word.strip() for word in f.readlines()]
    return jsonify({'word': random.choice(words)})

if __name__ == '__main__':
    app.run(debug=True)
