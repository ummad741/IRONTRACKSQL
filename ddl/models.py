from db.utils import execute_query


def task1_student_table():
    query = """
    CREATE TABLE IF NOT EXISTS student(
        id SERIAL PRIMARY KEY ,
        name VARCHAR(100) NOT NULL,
        age INT
    );
    """

    execute_query(query)


def task2_products_checkconstraint():
    query = '''
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY ,
        name VARCHAR(100) NOT NULL,
        price FLOAT,
        discount FLOAT,
        in_stock BOOLEAN DEFAULT TRUE,
        category_id INT ,
        CHECK (discount <=  price AND price > 0),
        FOREIGN KEY (category_id) REFERENCES category(id)
        ON DELETE SET NULL
    );
    '''

    execute_query(query)


def task3_users_uniqueconstraint():
    query = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        age INT NOT NULL,
        email VARCHAR(100),
        is_active BOOLEAN DEFAULT TRUE,
        UNIQUE(username, email)
    );
    """
    execute_query(query)


def task4_foreignkey():
    first_query = """
    CREATE TABLE IF NOT EXISTS departments(
        id SERIAL PRIMARY KEY ,
        name VARCHAR(50) NOT NULL,
        employee_id INT,
        FOREIGN KEY (employee_id) REFERENCES employees(id) 
        ON DELETE RESTRICT
    );
    """

    second_query = """
    CREATE TABLE IF NOT EXISTS employees(
        id SERIAL PRIMARY KEY ,
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
    #     SERIAL NT NOT NULL ,
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
        id SERIAL PRIMARY KEY ,
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


def task6_multiple_columns_unqiue():
    query = """
        CREATE TABLE IF NOT EXISTS user_sessions(
            user_id INT ,
            session_token VARCHAR(255),
            created_at DATETIME NOT NULL DEFAULT NOW(),
            UNIQUE(user_id, session_token)
        );
    """
    execute_query(query)


def task7_update_on_cascade():
    query1 = """
        CREATE TABLE IF NOT EXISTS countries(
            id SERIAL PRIMARY KEY ,
            name VARCHAR(100) NOT NULL,
            UNIQUE(name)  
        );
    """
    query2 = """
        CREATE TABLE IF NOT EXISTS cities(
            id SERIAL PRIMARY KEY ,
            country_id INT,
            FOREIGN KEY (country_id)
            REFERENCES countries(id)
            ON UPDATE CASCADE
        );
    """

    execute_query(query1)
    execute_query(query2)


def task8_datetime_now():
    query = """
        CREATE TABLE IF NOT EXISTS logs(
            id SERIAL PRIMARY KEY ,
            message TEXT,
            created_at DATETIME DEFAULT NOW()
        )
    """
    execute_query(query)


def task9_enum():
    query = """
        CREATE TABLE IF NOT EXISTS payments(
            id SERIAL PRIMARY KEY ,
            amount FLOAT,
            status ENUM('Pending', 'paid', 'failed') DEFAULT 'Pending',
            user_id INT ,
            order_id INT, 
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
        )
    """

    execute_query(query)


def task10_working_on_index():
    # what is index
    # Indexing makes columns faster to query by creating pointers to where data is stored within a database.
    # types of indexing
    # 1 middle entry
    # 2 smallest entry
    # 3 greates entry

    # index nma tez qidiruv va tablelarni saralaydi,
    # SELECT sorovini mukamalashtiradi yani zaprosnin ishlanish tezligi oshiradi 10 sec bogan indexingdan keyin 1 sec tushadi
    # minus taraflarni malumotni update qilvotganda indexni ham ozgartirishga tori keladi kop ish talab qilishi mumkun

    # 3 hil turdagi indexlash bor
    # 1 orta kirish
    # 2 kichik kirish
    # 3 katta kirish

    # query = """
    #     CREATE INDEX simpleindex ON user_sessions(created_at);
    # """

    # query_multiple_column = """
    #     CREATE INDEX multipleindex ON users(username, is_active);
    # """
    # query_unique_index = """
    #     CREATE UNIQUE INDEX unique_index ON countries(name);
    # """

    # execute_query(query)
    # execute_query(query_multiple_column)
    # execute_query(query_unique_index)
    pass


# def task11_drop_index():
#     query = """
#         DROP INDEX simpleindex ON user_sessions;
#     """
#     execute_query(query)

def task12_fulltext_index_search():
    query = """
        CREATE TABLE IF NOT EXISTS posts(
            id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            content TEXT,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE,
            FULLTEXT INDEX like_google_search_idx(content)
        );
    """
    execute_query(query)

# def deleter_table():
#     query = """
#         DROP TABLE IF EXISTS employes;
#     """
#     execute_query(query)


# connections with foreign key

def task13_on_delete():
    query = """
        CREATE TABLE IF NOT EXISTS category(
            id SERIAL PRIMARY KEY,
        );
    """