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
    print(f"user id {user}")
    user['id'] = (users[-1]['id']) + 1
    users.append(user)
    return user, 201

def show(req, id):
    return find_by_id(id), 200



def find_by_id(id):
    try:
        return next(user for user in users if user['id'] == id)
    except:
        raise BadRequest(f"User with id {id} not found.")
