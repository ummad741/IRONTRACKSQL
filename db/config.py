import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT")),
    "database": os.getenv("DB_NAME"),
}

# connection pooling
connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    **db_config
)
print(f"connectest: {connection_pool}")


def get_connection():
    return connection_pool.get_connection()


def get_cursor(connection):
    return connection.cursor(dictionary=True)
