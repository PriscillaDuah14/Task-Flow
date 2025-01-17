from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

database_username = os.getenv('DB_USERNAME')
database_password = os.getenv('DB_PASSWORD')
database_name = os.getenv('DB_NAME')

print(database_username, database_password, database_name)

connection_str = 'mysql+mysqlconnector://db_username:db_password@localhost/db_name'

engine = create_engine(connection_str)

try:
    connection = engine.connect()
    print('Located and connected to database')
    connection.close()
except Exception as e:
    print(f'An error occured: {e}')

DBSession = sessionmaker(bind=engine) 
session = DBSession()


  
