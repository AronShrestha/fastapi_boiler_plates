from typing import Annotated
import fastapi
from fastapi import FastAPI, Header, Path, Query

router = fastapi.APIRouter(prefix='/section')



@router.get("/{id}")
async def read_section():
    return {"courses": []}


@router.get("/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/{id}")
async def read_content_block():
    return {"courses": []}