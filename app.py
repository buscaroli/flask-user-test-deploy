from flask import Flask, jsonify, request
from flask_cors import CORS 
from controllers import users
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError


app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello and Welcome!"

@app.route('/api/users', methods=['GET', 'POST'])
def user_handler():
    if request.method == 'GET':
        resp, code = users.all(request)
        return jsonify(resp), code
    else:
        resp, code = users.create(request)
        return jsonify(resp), code


if __name__ == "__main__":
    app.run()
