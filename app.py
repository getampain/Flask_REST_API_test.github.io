from flask import Flask
from flask_restful import Resource, Api
import pymysql


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
    def get(self, id, pw):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='flask')
        cur = conn.cursor()
        sql = "SELECT * FROM flask.userInfo WHERE userid = '"+id+"' and userpw = '"+pw+"' "
        row = cur.execute(sql)
        result = cur.fetchall()

        #conn.commit()
        print("!!!!"+sql)
        print(row)

        #return row

        if(row == 0 ):
            return {'get_test': "not exist"}
        else:
            return {'get_test': result[0]}


        """if id == "abc" and pw == "1234":
            return {'get_test': row[0]}
        else:
            return {'get_test': 'fail'}, 404 """


api.add_resource(TestPost, '/', '/testp/<int:id>')
api.add_resource(TestGet, '/', '/login/<string:id>/<string:pw>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')