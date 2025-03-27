from sqlalchemy import select
from sqlalchemy.orm.session import Session
from app.models import Files, Tags, Attributes


def create_file(
    session: Session,
    filename: str,
    data: list,
) -> bool:
    # TODO: либо insert все, либо insert ничего
    file = Files(name=filename)
    session.add(file)
    session.commit()
    file_id = file.id

    for tag_item in data:
        tag = Tags(name=tag_item["name"], file_id=file_id)
        session.add(tag)
        session.commit()
        tag_id = tag.id

        if tag_item["attributes"]:
            for attr_item in tag_item["attributes"]:
                session.add(Attributes(**attr_item, tag_id=tag_id))
                session.commit()

    return True


def get_file_by_name(session: Session, filename: str) -> Files:
    stmt = select(Files).filter_by(name=filename)
    file = session.scalar(stmt)
    if not file:
        raise Exception("ERROR: Empty file")
    return file


def get_count_tag(
    session: Session,
    filename: str,
    tag: str,
) -> int | None:
    file = get_file_by_name(session=session, filename=filename)
    tags = (
        session.query(Tags)
        .filter(
            Tags.file_id == file.id,
            Tags.name == tag,
        )
        .count()
    )
    if tags:
        return tags
    return None


def get_attributes_for_tag(
    session: Session,
    filename: str,
    tag: str,
) -> list | None:
    file = get_file_by_name(session=session, filename=filename)
    stmt = (
        select(Attributes.name)
        .where(
            Attributes.tag_id.in_(
                select(Tags.id).where(
                    Tags.file_id == file.id,
                    Tags.name == tag,
                )
            )
        )
        .distinct()
    )
    attributes = session.execute(stmt).scalars().all()
    if attributes:
        return list(attributes)
    return None
