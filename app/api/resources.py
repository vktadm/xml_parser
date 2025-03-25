from flask_restful import Resource


class Main(Resource):
    def get(self):
        return {"message": "Hello, World!"}, 200


class File(Resource):

    def post(self):
        return {"message": "True"}, 201


class Tag(Resource):
    def get(self):
        return {"message": "В файле отсутствует тег с данным названием"}, 200


class Attribute(Resource):
    def get(self):
        return {"message": "У тега: {} не существует атрибутов"}, 200
