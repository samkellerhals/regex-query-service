from pydantic import BaseModel, Field
from typing import List, Optional, Pattern


# query out data no id model
class QueryOutNoId(BaseModel):
    regex_query: str
    search_word: str
    num_outlets: int
    per_outlets: float
    brand_id: List[str]


# query in data model
class QueryIn(BaseModel):
    column_name: str = Field(default="name", example="name")
    search_word: Optional[str] = Field(default="Pepsi", example="Pepsi")
    query: Optional[str] = Field(default="default", example="default")
    save: Optional[bool] = Field(default=False, example=False)


# query out data model
class QueryOut(QueryOutNoId):
    id: int
