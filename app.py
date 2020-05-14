from flask import Flask
from flask_restful import Resource, Api
import sqlite3
import json

app = Flask(__name__)
api = Api(app)


class TestPost(Resource):
    def post(self, id):
        if id == 10:
            return {'post_test': 'success'}
        else:
            return {'post_test': 'fail'}, 404


class TestGet(Resource):
    def get(self, id):
        if id == 10:
            return {'get_test': 'success'}
        else:
            return {'get_test': 'fail'}, 404


api.add_resource(TestPost, '/', '/testp/<int:id>')
api.add_resource(TestGet, '/', '/testg/<int:id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')