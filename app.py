from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello and Welcome!"

if __name__ == "__main__":
    app.run()
