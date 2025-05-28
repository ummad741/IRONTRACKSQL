from db.utils import execute_query


def task1_student_table():
    query = """
    CREATE TABLE IF NOT EXISTS student(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        age INT
    );
    """

    execute_query(query)


def task2_products_checkconstraint():
    query = '''
    CREATE TABLE IF NOT EXISTS products(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        price FLOAT,
        in_stock BOOLEAN DEFAULT TRUE,
        CHECK (price > 0)
    );
    '''

    execute_query(query)


def task3_users_uniqueconstraint():
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE,
        is_active BOOLEAN DEFAULT TRUE,
        # UNIQUE(username) 
    );
    """
    execute_query(query)


def task4_foreignkey():
    first_query = """
    CREATE TABLE IF NOT EXISTS departments(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL
    );
    """

    second_query = """
    CREATE TABLE IF NOT EXISTS employees(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL, 
        dept_id INT,
        FOREIGN KEY(dept_id)
        REFERENCES departments(id)
        ON DELETE CASCADE
    );
    """
    execute_query(first_query)
    execute_query(second_query)

    # FOREIGN KEY EXAMPLE HOW TO USING:

    # CREATE TABLE product (
    # category INT NOT NULL, id INT NOT NULL,
    # price DECIMAL,
    # PRIMARY KEY(category, id)
    # )ENGINE=INNODB;

    # CREATE TABLE customer (
    #     id INT NOT NULL,
    #     PRIMARY KEY (id)
    # )   ENGINE=INNODB;

    # CREATE TABLE product_order (
    #     no INT NOT NULL AUTO_INCREMENT,
    #     product_category INT NOT NULL,
    #     product_id INT NOT NULL,
    #     customer_id INT NOT NULL,

    #     PRIMARY KEY(no),
    #     INDEX (product_category, product_id),
    #     INDEX (customer_id),

    #     FOREIGN KEY (product_category, product_id)
    #     REFERENCES product(category, id)
    #     ON UPDATE CASCADE ON DELETE RESTRICT,

    #     FOREIGN KEY (customer_id)
    #     REFERENCES customer(id)
    # )   ENGINE=INNODB;


def task5_orders_fullconstraint():
    query = """
    CREATE TABLE IF NOT EXISTS orders(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT, 
        amount FLOAT CHECK(amount >= 0),
        status VARCHAR(20) DEFAULT 'Pending',
        created_at DATE NOT NULL,
        FOREIGN KEY(user_id) 
        REFERENCES users(id)
        ON DELETE CASCADE
    );
    """

    execute_query(query)
