from flask import Flask
from flask_restful import Api
import app.api as resources


def create_app():
    app = Flask(__name__)
    # Регестрируем api.
    api = Api(app)

    # Добавляем endpoints.
    api.add_resource(resources.Main, "/")
    api.add_resource(resources.File, "/api/file/read")
    api.add_resource(resources.Tag, "/api/tags/get-count")
    api.add_resource(resources.Attribute, "/api/tags/attributes/get")

    return app
