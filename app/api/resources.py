from flask_pydantic import validate
from flask_restful import Resource

from xml.sax import SAXException
from sqlalchemy.exc import SQLAlchemyError

from app.db_helper import db_helper
from .services import create_file, get_count_tag, get_attributes_for_tag
from .xml_parser import xml_parser
from .schemas import FileSchema, TagSchema


class Main(Resource):
    def __init__(self, logger):
        self.logger = logger

    def get(self):
        # self.logger.info("Get MAIN")
        return {"message": "Get MAIN page"}, 200


class File(Resource):
    def __init__(self, logger):
        self.logger = logger

    @validate()
    def post(self, body: FileSchema):
        filename = str(body.name)
        try:
            data = xml_parser(filename)
            with db_helper.get_session() as s:
                create_file(
                    session=s,
                    filename=filename,
                    data=data,
                )
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
            self.logger.error(f"Server ERROR: {str(e)}")
            return {
                "result": "False",
                "message": "Server ERROR",
            }, 500

        return {"result": "True"}, 201


class Tag(Resource):
    def __init__(self, logger):
        self.logger = logger

    @validate()
    def get(self, body: TagSchema):
        filename = str(body.filename)
        tag = body.name

        with db_helper.get_session() as s:
            try:
                quantity = get_count_tag(
                    session=s,
                    filename=filename,
                    tag=tag,
                )
            except Exception as e:
                self.logger.error(f"ERROR: {str(e)}")
                return {
                    "message": "File ERROR",
                }, 400

        if quantity:
            return {"result": quantity}, 200

        return {
            "message": f"В файле отсутствует тег: {tag}",
        }, 200


class TagAttributes(Resource):
    def __init__(self, logger):
        self.logger = logger

    @validate()
    def get(self, body: TagSchema):
        filename = str(body.filename)
        tag = body.name

        with db_helper.get_session() as s:
            try:
                attributes = get_attributes_for_tag(
                    session=s,
                    filename=filename,
                    tag=tag,
                )
            except Exception as e:
                self.logger.error(f"ERROR: {str(e)}")
                return {
                    "message": "File ERROR",
                }, 400

        if attributes:
            return {"result": attributes}, 200

        return {
            "message": f"У тега: {tag} не существует атрибутов",
        }, 200
