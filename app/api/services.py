import xml.sax
from pathlib import Path

from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.db_helper import db_helper
from app.models import Files, Tags


def create_file(
    filename,
    data,
) -> int:
    file = Files(name=filename)
    Session = db_helper.get_session()
    with Session() as session:
        session.add(file)
        file = file.id

        session.commit()
    return file
