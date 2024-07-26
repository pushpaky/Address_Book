from sqlalchemy.orm import Session
from geopy.distance import geodesic
from fastapi import HTTPException

from . import models, schemas


# Read a particular data from the database
def get_address(db: Session, address_id: int):
    return db.query(models.Address).filter(models.Address.id == address_id).first() # noqa


# Read all data from the database
def get_addresses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Address).offset(skip).limit(limit).all()


# create a New Address book data for the database
def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


# Upadte the particular data from the database
def update_address(db: Session, address_id: int, address: schemas.AddressUpdate): # noqa
    db_address = get_address(db, address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    return db_address


# Delete the particular data from the database
def delete_address(db: Session, address_id: int):
    db_address = get_address(db, address_id)
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    return db_address


# Read the data within the distance from the database
def get_addresses_within_distance(db: Session, lat: float, lon: float, distance: float): # noqa
    addresses = db.query(models.Address).all()
    result = []
    for address in addresses:
        if geodesic((lat, lon), (address.latitude, address.longitude)).km <= distance: # noqa
            result.append(address)
    return result
