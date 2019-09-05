from flask import Blueprint
from flask_restful import Api

from . import views
hello_bp = Blueprint("helloworld", __name__)
hello_api = Api(hello_bp, catch_all_404s=True)

# hello_api.representation('application/json')

hello_api.add_resource(views.HelloWorld, '/hello' ,
                       endpoint='HelloWorld')