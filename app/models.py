from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True  # Таблица не создается в БД

    @declared_attr.directive  # Ииспользуется для динамического определения атрибутов в декларативных моделях
    def __tablename__(cls) -> str:
        # Автоматически генерирует имя таблицы
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(
        primary_key=True
    )  # одинаковое поле id для всех потомков


class Files(Base):
    name: Mapped[str] = mapped_column(unique=True)


class Tags(Base):
    name: Mapped[str] = mapped_column(unique=True)


class Attributes(Base):
    name: Mapped[str] = mapped_column(unique=True)
    value: Mapped[str]
