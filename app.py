from flask import Flask, jsonify, request
from flask_cors import CORS 
from controllers import users
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError


app = Flask(__name__)

@app.route('/')
def index():
    return f"Hello and Welcome!"

@app.route('/api/users', methods=['GET', 'POST'])
def users_handler():
    if request.method == 'GET':
        resp, code = users.all(request)
        return jsonify(resp), code
    else:
        resp, code = users.create(request)
        return jsonify(resp), code

@app.route('/api/users/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def user_handler(id):
    if request.method == 'GET':
        resp, code = users.show(id)
        return jsonify(resp), code
    elif request.method == 'DELETE':
        resp, code = users.delete(id)
        return jsonify(resp), code
    elif request.method == 'PATCH':
        resp, code = users.update(request, id)
        return jsonify(resp), code
# else catch-all not required as flask sends a' Method Not Allowed' by default


@app.errorhandler(NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run()
