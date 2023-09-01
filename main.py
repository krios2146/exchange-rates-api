from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

import currency_repository
from database import SessionLocal, Base, engine
from schema.currency import Currency, CurrencyAdd

app = FastAPI()

Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root(request: Request):
    return {"message": f"For the swagger docs visit {request.url}docs"}


@app.get("/api/currencies", response_model=list[Currency])
async def get_currencies(db: Session = Depends(get_db)):
    return currency_repository.find_all(db)


@app.post("/api/currencies", response_model=Currency)
async def post_currency(currency: CurrencyAdd, db: Session = Depends(get_db)):
    return currency_repository.save(db, currency)


@app.get("/api/currency/{code}", response_model=Currency)
async def get_currency(code, db: Session = Depends(get_db)):
    return currency_repository.find_by_code(db, code)
