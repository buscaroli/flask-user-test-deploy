import json

class TestAPI():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        assert '200' in res.status
        #  using 'in' can be easier when a lot of text
        assert "Welcome" in res.json['message']

    def test_all(self, api):
        res = api.get('/api/users')
        assert res.status == '200 OK'
        assert len(res.json) == 2

    def test_create(self, api):
        mock_data = json.dumps({'name': 'Stewart', 'email': 'stewart@email.com', 'password': 'stewartpw'})
        mock_headers = {'Content-Type': 'application/json'}

        res = api.post('/api/users', data=mock_data, headers=mock_headers)
        assert res.status == '201 CREATED'
        assert '201' in res.status
        assert res.json['id'] == 3
        assert res.json['name'] == 'Stewart'

    def test_show(self, api):
        res = api.get('/api/users/1')
        assert res.status == '200 OK'
        #  using the mock API
        assert res.json['name'] == 'Mark'

    def test_show_error(self, api):
        res = api.get('/api/users/100')
        assert res.status == '400 BAD REQUEST'
        assert '400' in res.status
    
    def test_delete(self, api):
        res = api.delete('/api/users/1')
        assert res.status == '204 NO CONTENT'

    def test_delete_error(self, api):
        res = api.delete('/api/users/100')
        assert res.status == '400 BAD REQUEST'

    def test_update(self, api):
        mock_data = json.dumps({'name': 'Stewart', 'email': 'stewart@email.com', 'password': 'stewartpw'})
        mock_headers = {'Content-Type': 'application/json'}

        res = api.patch('/api/users/1', data=mock_data, headers=mock_headers)
        assert res.status == '200 OK'
        assert '200' in res.status
        assert res.json['id'] == 1
        assert res.json['name'] == 'Stewart'

    def test_update_error(self, api):
        mock_data = json.dumps({'name': 'Stewart', 'email': 'stewart@email.com', 'password': 'stewartpw'})
        mock_headers = {'Content-Type': 'application/json'}

        res = api.patch('/api/users/100', data=mock_data, headers=mock_headers)
        assert res.status == '400 BAD REQUEST'
        assert '400' in res.status

    def test_404(self, api):
        res = api.get('/non_existent_endpoint')
        assert res.status == '404 NOT FOUND'
        assert '404' in res.status
