from typing import List

from app.api.models import QueryOut, QueryIn, QueryOutNoId
from app.api.db_manager import get_from_db, save_to_db, update_db, delete_from_db
from app.api.regex import RegexMatcher
from fastapi import APIRouter, HTTPException

# define regex app
regex_service = APIRouter()


@regex_service.get("/get-queries", response_model=List[QueryOut], status_code=200)
async def index():
    # return all entries inside regex_db
    return await get_from_db()


@regex_service.post("/add-query", response_model=QueryOutNoId, status_code=201)
async def add_query(payload: QueryIn):

    # Compute regex matches
    matcher = RegexMatcher(payload.search_word)

    result = matcher.get_matches(payload.column_name)

    if payload.save:
        # add result to database
        await save_to_db(result)

    return result


@regex_service.put("/{id}")
async def update_query(id: int, payload: QueryOutNoId):

    # check that specified query exists
    query = await get_from_db(id)

    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    else:
        # update the database
        await update_db(id, payload)

        return {"id": id, "status": "successfully updated"}


@regex_service.delete("/{id}")
async def delete_query(id: int):

    # check that specified query exists
    query = await get_from_db(id)

    if not query:
        raise HTTPException(status_code=404, detail="Query not found")
    else:
        # delete a record from the database
        await delete_from_db(id)

        return {"id": id, "status": "successfully deleted"}
