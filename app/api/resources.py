from flask_pydantic import validate
from flask_restful import Resource

from xml.sax import SAXException

from sqlalchemy.exc import SQLAlchemyError

from .services import create_file
from .xml_parser import xml_parser
from .schemas import FileSchema, TagSchema, AttributeSchema


class Main(Resource):
    def __init__(self, logger):
        self.logger = logger

    def get(self):
        self.logger.info("Get MAIN")
        return {"message": "Main page"}, 200


class File(Resource):
    def __init__(self, logger):
        self.logger = logger

    @validate()
    def post(self, body: FileSchema):
        filename = str(body.name)
        try:
            data = xml_parser(filename)
            create_file(filename, data)
        except SAXException as e:
            self.logger.error(f"SAXParser ERROR: {str(e)}")
            return {
                "result": "False",
                "message": "SAXParser ERROR",
            }, 400
        except SQLAlchemyError as e:
            self.logger.error(f"SQLAlchemy ERROR: {str(e)}")
            return {
                "result": "False",
                "message": "SQLAlchemy ERROR",
            }, 500
        except Exception as e:
            self.logger.error(f"SQLAlchemy ERROR: {str(e)}")

        return {"result": "True"}, 201


class Tag(Resource):
    @validate()
    def get(self, body: TagSchema):
        print(body)
        return {
            "result": None,
            "message": "В файле отсутствует тег с данным названием",
        }, 200


class TagAttributes(Resource):
    @validate()
    def get(self, body: TagSchema):
        print(body)
        return {
            "result": None,
            "message": "У тега: {} не существует атрибутов",
        }, 200
