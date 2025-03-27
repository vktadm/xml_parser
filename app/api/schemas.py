from pydantic import BaseModel, FilePath


class FileSchema(BaseModel):
    name: FilePath


class TagSchema(BaseModel):
    name: str
    file_id: int


class AttributeSchema(BaseModel):
    name: str
    value: str
    tag_id: int
