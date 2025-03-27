from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import settings


class DatabaseHelper:
    def __init__(self, url, echo: bool = False):
        self.engine = create_engine(url=url, echo=echo)
        self.session = sessionmaker()
        self.session.configure(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
        )

    def get_session(self):
        return self.session()


db_helper = DatabaseHelper(url=settings.db.url, echo=settings.db.echo)
