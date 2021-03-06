from werkzeug.exceptions import BadRequest

users = [
    {'id':1, 'name': 'Matt', 'email': 'matt@email.com', 'password': 'mattpw'},
    {'id':2, 'name': 'John', 'email': 'john@email.com', 'password': 'johnpw'},
    {'id':3, 'name': 'Sue', 'email': 'sue@email.com', 'password': 'suepw'}
]

def all(req):
    return [user for user in users], 200

def create(req):
    user = req.get_json()
    user['id'] = (users[-1]['id']) + 1
    users.append(user)
    return user, 201

def show(id):
    return find_by_id(id), 200

def delete(id):
    user = find_by_id(id)
    users.remove(user)
    return user, 204

def update(req, id):
    user = find_by_id(id)
    data = req.get_json()
    for key, val in data.items():
        user[key] = val
    return user, 200

def find_by_id(id):
    try:
        return next(user for user in users if user['id'] == id)
    except:
        raise BadRequest(f"User with id {id} not found.")
