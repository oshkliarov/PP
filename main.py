from flask import Flask

app = Flask(__name__)


@app.route("/api/v1/hello-world-26")
def hello_world():
    return "Hello, World 26!", 200
