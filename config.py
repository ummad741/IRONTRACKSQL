import mysql
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
}

try:
    db = mysql.connector.connect(**db_config)
    print(db)
except mysql.connector.Error as err:
    print(f"connection error {err}")