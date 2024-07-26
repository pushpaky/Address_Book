from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas, database, dependencies

app = FastAPI()


# On application startup initializing the database
@app.on_event("startup")
def startup():
    database.Base.metadata.create_all(bind=database.engine)


# create a address book for the database
@app.post("/addresses/", response_model=schemas.Address)
def create_address(
    address: schemas.AddressCreate, db: Session = Depends(dependencies.get_db)
):
    return crud.create_address(db=db, address=address)


# Read all address book from the database
@app.get("/addresses/", response_model=List[schemas.Address])
def read_addresses(
    skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)
):
    addresses = crud.get_addresses(db, skip=skip, limit=limit)
    return addresses


# Read a particular address book from the database
@app.get("/addresses/{address_id}", response_model=schemas.Address)
def read_address(address_id: int, db: Session = Depends(dependencies.get_db)):
    db_address = crud.get_address(db, address_id=address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


# Update a particular address book from the database
@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(
    address_id: int,
    address: schemas.AddressUpdate,
    db: Session = Depends(dependencies.get_db),
):
    return crud.update_address(db=db, address_id=address_id, address=address)


# Delete a particular address book from the database
@app.delete("/addresses/{address_id}", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(dependencies.get_db)): # noqa
    return crud.delete_address(db=db, address_id=address_id)


# Read the address book within the distance from the database
@app.get("/addresses/within_distance/", response_model=List[schemas.Address])
def get_addresses_within_distance(
    lat: float, lon: float, distance: float, db: Session = Depends(dependencies.get_db) # noqa
):
    addresses = crud.get_addresses_within_distance(
        db, lat=lat, lon=lon, distance=distance
    )
    return addresses
