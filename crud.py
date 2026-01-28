from sqlalchemy.ext.asyncio import AsyncSession
from models import *
from schemas import *

async def craete_doktor(doktor: DoktorCreate, db: AsyncSession) -> DoktorResponse:
    db_doktor = Doktor(**doktor.model_dump())
    db.add(db_doktor)
    await db.commit()
    await db.refresh(db_doktor)
    return DoktorResponse.model_validate(db_doktor)