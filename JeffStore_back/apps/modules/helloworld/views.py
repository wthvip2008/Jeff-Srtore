from flask_restful import Resource
from flask_restful.reqparse import RequestParser


# 测试flask_restful 使用
class HelloWorld(Resource):
    def get(self):
        qs_parser = RequestParser()
        qs_parser.add_argument("name",required=True,help="miss name")
        result = qs_parser.parse_args()
        name = result.get("name")
        return "name:{}".format(name)


