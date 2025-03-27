from pydantic import BaseModel, FilePath


class FileSchema(BaseModel):
    name: FilePath


class TagSchema(BaseModel):
    name: str
    filename: FilePath
