from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello, 2025!")
    return "Hello, 2025!"

if __name__ == "__main__":
    app.run()
