import pytest
import app
from controllers import users

@pytest.fixture
def api(monkeypatch):
    test_users = [
         {'id':1, 'name': 'Mark', 'email': 'mark@email.com', 'password': 'markpw'},
    {'id':2, 'name': 'Sue', 'email': 'sue@email.com', 'password': 'suepw'},
    ]
    monkeypatch.setattr(users, "users", test_users)
    api = app.app.test_client()
    return api
