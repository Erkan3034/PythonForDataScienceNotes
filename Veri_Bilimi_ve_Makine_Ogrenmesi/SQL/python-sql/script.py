import sqlite3
import os

def create_database():
    #if os.path.exists('courses.db'):
        #os.remove('courses.db')
    conn = sqlite3.connect('courses.db')
    cursor= conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    course_code TEXT NOT NULL,
    course_teacher TEXT NOT NULL
    
    )''')

def insert_tuple_data(cursor):

    courses= [
        (1,'Python','Erkan',5),
        (2,'Java','Serkan',6),
        (3,'Php', 'Necip', 8)
    ]

    cursor.executemany('INSERT INTO courses VALUES (?,?,?,?)', courses)

def main():
    conn, cursor = create_database()
    try:
        create_database()
        create_tables(cursor)
        conn.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        conn.close()
if __name__ == "__main__":
    main()