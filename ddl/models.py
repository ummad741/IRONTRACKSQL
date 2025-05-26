from db.utils import execute_query


def task1_student_table():
    query = """
    CREATE TABLE IF NOT EXISTS student(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        age INT(11)
    );
    """

    execute_query(query)

