from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import uvicorn
from database import *
from schemas import *
from crud import craete_doktor

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/doktor", response_model=DoktorResponse)
async def add_doktor(doktor: DoktorCreate, db: AsyncSession = Depends(get_db)):
    return await craete_doktor(doktor, db)

if __name__ == '__main__':
    uvicorn.run(app)