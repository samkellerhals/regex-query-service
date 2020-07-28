from typing import Optional
from app.api.models import QueryOut
from app.api.db import regex_matches, database


# Getting all saved queries in database
async def get_from_db(id: Optional[int] = None):

    if id:
        query = regex_matches.select().where(regex_matches.c.id == id)
    else:
        query = regex_matches.select()

    return await database.fetch_all(query=query)


# Adding new query information to database
async def save_to_db(payload: QueryOut):

    query = regex_matches.insert().values(**payload)

    return await database.execute(query=query)


# Updating query information in database
async def update_db(id: int, payload: QueryOut):

    query = (
        regex_matches.update().where(regex_matches.c.id == id).values(**payload.dict())
    )

    return await database.execute(query=query)

# Deleting query information in database
async def delete_from_db(id: int):

    query = regex_matches.delete().where(regex_matches.c.id == id)

    return await database.execute(query=query)
