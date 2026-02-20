import sqlite3
import os

def create_database():
    if os.path.exists('students.db'):
        os.remove('students.db')
    
    conn = sqlite3.connect('students.db')
    cursor= conn.cursor()
    return conn, cursor


def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    city TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name VARCHAR(50) NOT NULL,
        instructor TEXT NOT NULL,
        credits INTEGER NOT NULL
    )
    ''')


def insert_data(cursor):
    cursor.execute('''
    INSERT INTO Students (name,age,email,city) VALUES
    ('Ahmet',20,'ahmet@mail.com','Ankara'),
    ('Mehmet',22,'mehmet@mail.com','Istanbul'),
    ('Ayse',21,'ayse@mail.com','Izmir'),
    ('Fatma',23,'fatma@mail.com','Bursa'),
    ('Ali',24,'ali@mail.com','Ankara')
    ''')
def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        print("✅ INFO: Tables created successfully.")
        insert_data(cursor)
        print("✅ INFO: Data inserted successfully.")
        conn.commit()
    except sqlite3.Error as error:
        print(f"❌ ERROR: There was an error while creating tables: {error}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
