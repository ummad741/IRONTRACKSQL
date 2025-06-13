# IRONTRACK MYSQL

## 📘 DESCRIPTION

**IRON TRACK ALGORITHM LEARNING FOR SQL AND ADVANCED WITH MINI PROJECTS.**

---

## 🚀 Getting Started

### 🧩 DEPENDENCIES

- Any OS with Python (e.g., Ubuntu 20.04, Windows 10, etc.)
- Python 3.8+
- pip package manager

---

### 📦 INSTALLING

Download and install dependencies:

- [MySQL Connector Documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)

#### ✅ Via pip:

```bash
pip install mysql-connector-python
```

### ▶️ EXECUTING PROGRAM

#### Step 1: MySql Configure

1. SQL ROOT USER

   - Create MySQL Root User For Ubuntu

   ```bash
   sudo mysql -u root
   ```

   - Create Your User

   ```sql
   # example
   CREATE USER 'myuser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mypassword';
   ```

   - Change User permsions

   ```sql
      ALTER USER 'youruser'@'yourhost' WITH
      mysql_native_password BY 'yourpassword';
   ```

2. SQL DATABASE
   - enter command
   ```bash
   sudo mysql -u root -p
   ```
   - Select all data from database
   ```sql
   SHOW DATABASE;
   ```
   - Creat database
   ```sql
   CREATE DATABASE examplename;
   ```
   - Select all users from database
   ```sql
   SELECT user,host FROM mysql.user;
   ```
3. ENTER TO DATABASE:
   ```sql
      SHOW DATABASES;
      USE your_database;
      SHOW TABLES;
      SELECT * FROM table_name;
      <!-- TABLE STRUCTURE -->
      DESCRIBE table_name;
      DESC table_name;
   ```
4. GRANTING PERMISSIONS
   - getting all user from mysql
   ```sql
      SELECT user, host, FROM mysql.user;
   ```
   - View permissions for users
   ```sql
      SHOW GRANTS FOR 'root'@'localhost';
   ```
   - Granting permissions for user
   ```sql
      <!-- for all servser -->
      GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'
      WITH GRANT OPTION;
      <!-- for database -->
      GRANT SELECT, INSERT, UPDATE, DELETE ON
      database.* TO 'appuser'@'localhost';
      <!-- another way -->
      GRANT ALL PRIVILEGES ON database.* TO
      'user'@'host';
   ```

#### Step 2: File Structure and working Structure

1. DRY(Dont repeat yourself) - Kodlar takrolanmidi
   - get_connection() va get_cursor() funksiyalari config.py ichida modullashtirilgan.
2. SRP(Single Responsibility Principle) – har modul o‘z vazifasini bajaradi:
   - config.py faqat connection/cursor bilan shug‘ullanadi.
   - models.py faqat SQL so‘rov bajaradi.
3. Reusability – bir joyda o‘zgarish bo‘lsa, hamma joyga ta’sir qiladi:
   - Masalan, database host o‘zgarsa — faqat config.py da o‘zgartiriladi.
4. Loose coupling – modul va komponentlar bir-biriga qattiq bog‘liq emas:
   - models.py hech qanday host, user, passwordni bilmaydi — u faqat configdagi API orqali ulanyapti.
5. Connection pooling:
   - mysql.connector.pooling.MySQLConnectionPool ishlatiladi.
   - Har safar yangi connection emas, oldindan ochilgan connection’lar pool’idan olinadi.
6. Custom DB utility layer (service layer yoki repository pattern)
   - Har bir modulda query yozish o‘rniga, alohida db_service.py moduli qilinadi.

### step 3 Working Methods, Tasks and Solutions

1. DDL (Data Definition Language):
   - CREATE
   - ALTER
   - DROP
2. DML (Data Manipulation Language):
   - DELETE
   - UPDATE
   - SELECT
   - INSERT
3. DCL (Data Control Language):
   - GRANT
   - REVOKE
4. TCL (Transaction Control Language):
   - BEGIN
   - COMMIT
   - ROLLBACK
