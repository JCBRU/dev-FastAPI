from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

import os

load_dotenv()

MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_ADDRESS = os.getenv("MYSQL_ADDRESS")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://dbdev:k9MPi9yn87BL7F7h@127.0.0.1:3306/devaster"
SQLALCHEMY_DATABASE_URL="mysql+mysqldb://%s:%s@%s/%s" % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_ADDRESS, MYSQL_DATABASE)
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_recycle=3600
)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()