from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()



Db_url = os.environ.get("db_url")        

engine = create_engine(Db_url , connect_args = { "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine , autoflush=False)

Base = declarative_base()