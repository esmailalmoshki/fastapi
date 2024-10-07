import alembic.config
from sqlmodel import Session, create_engine
from models import *
import dotenv
import os
import alembic

dotenv.load_dotenv()

engine_url = os.getenv("ENGINE_URL")
alembic.config.Config.set_main_option(name="sqlalchemy.url",value=engine_url)


engine = create_engine(engine_url, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

