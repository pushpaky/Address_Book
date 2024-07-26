from pydantic import BaseModel


# Data validation class
class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    latitude: float
    longitude: float


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    pass


class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
