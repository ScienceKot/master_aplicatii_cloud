from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hi 21st of Mya 2024..."

app.run(port=5555, host="0.0.0.0")