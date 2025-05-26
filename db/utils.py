from db.config import get_connection, get_cursor

#  Custom DB Utility Layer (Har bir modulda query yozish o‘rniga, alohida service.py moduli ishlatiladi)
def execute_query(query, params=None):  # INSRT,UPT,DEL
    db = get_connection()
    cursor = get_cursor(db)

    try:
        cursor.execute(query, params)
        db.commit()
    finally:
        cursor.close()
        db.close()
