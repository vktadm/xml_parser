import logging

from flask import Flask
from flask_restful import Api

import app.api as resources

logging.basicConfig(
    # filename="record.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)
app = Flask(__name__)


api = Api(app=app, catch_all_404s=True, prefix="/api")

# Добавляем endpoints.
api.add_resource(
    resources.Main,
    "/",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(
    resources.File,
    "/file/read",
    resource_class_kwargs={"logger": app.logger},
)
api.add_resource(
    resources.Tag,
    "/tags/get-count",
    resource_class_kwargs={"logger": app.logger},
)
