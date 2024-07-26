from .database import SessionLocal


# initialize the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
