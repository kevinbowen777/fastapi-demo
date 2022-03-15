from pydantic import BaseModel, HttpUrl


class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl
