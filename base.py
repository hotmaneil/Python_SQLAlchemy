from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the MariaDB engine using MariaDB Connector/Python
engine = create_engine(
    "mariadb+mariadbconnector://root:Sunsda@127.0.0.1:3306/company")
Session = sessionmaker(bind=engine)
Base = declarative_base()
