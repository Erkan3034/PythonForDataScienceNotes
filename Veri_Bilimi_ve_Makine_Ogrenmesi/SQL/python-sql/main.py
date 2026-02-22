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
    ('Ali',24,'ali@mail.com','Ankara'),
    ('Erkan',22,'turguterkan@gmail.com', 'Istanbul')   
    ''')



def insert_tuple_data(cursor):

    courses= [
        (1,'Python','Erkan',5),
        (2,'Java','Serkan',6),
        (3,'Php', 'Necip', 8)
    ]

    cursor.executemany('INSERT INTO Courses VALUES (?,?,?,?)', courses)


def select_operations(cursor):
    cursor.execute('SELECT * FROM  Students')
    data = cursor.fetchall() # fetch all data(data comes as tuple)
    print(f"\n{10*"*"}Students table - SELECT ALL -:{10*"*"}\n")
    for row in data:
        print(row)

    cursor.execute('SELECT name,age FROM Students')
    records = cursor.fetchall()
    print("***********SELECT COLUMN*********** \n" , records)


    name_conditions = cursor.execute('SELECT * FROM Students WHERE name = ?', ("Ayse",))
    print("***********WHERE name = Ayse ************:\n" , name_conditions.fetchone())

    print("************ORDER BY **************\n") #aldığımız sonucları belirlenen kritere göre sıralar
    cursor.execute('SELECT * From Courses ORDER BY  credits ')
    data = cursor.fetchall()
    for row in data:
        print(row)

    print("************LIMIT BY **************\n")  # aldığımız sonucları belirlenen kritere göre sıralar
    cursor.execute('SELECT * From Courses  LIMIT 2 ')
    data = cursor.fetchall()
    for row in data:
        print(row)


def update_delete_operations(cursor):
    print("***********UPDATE *************\n")
    cursor.execute(" Update Students set age = 25 where name = 'Ahmet'")
    print(cursor.execute("SELECT * from Students where name = 'Ahmet'").fetchall())

    print("************DELETE *************\n")
    cursor.execute(" Delete from Students where name = 'Ahmet'")
    print(cursor.execute("SELECT * from Students").fetchall())



def aggregate_functions(cursor):
    print(f"\n{10*"-"} Aggregate Functions COUNT {10*"-"}")
    cursor.execute('SELECT COUNT(*) FROM Students') #COUNT(*) → Students tablosundaki toplam satır sayısını verir
    result = cursor.fetchone()
    print(result[0]) #tuple dan gercek sayıyı al.

    print(f"{10*"-"} Aggregate Functions AVERAGE {10*"-"}")
    cursor.execute('SELECT AVG(age) FROM Students') # age sütunun aritmetik ortalamasını alır.
    result = cursor.fetchone()
    print(result[0])

    print(f"{10 * "-"} Aggregate Functions MAX-MIN {10 * "-"}")
    cursor.execute('SELECT MAX(age) , MIN(age) FROM Students') #En büyük - en kucuk yas
    result = cursor.fetchone()
    max_age , min_age = result
    print("Max Age: ",max_age)
    print("Min Age: " ,min_age)

    print(f"{10 * "-"} Aggregate Functions GROUP BY{10 * "-"}")
    cursor.execute("SELECT city, COUNT(*) From Students GROUP BY city") # öğrencileri sehirlerine göre sıralar, her sehir için öğrenci sayısını aır.
    result = cursor.fetchall()
    for city,count in result:
        print(city, ": " , count)

    print(f"{10 * "-"} Aggregate Functions HAVING {10 * "-"}")
    cursor.execute("""
                   SELECT city, COUNT(*)
                   FROM Students
                   GROUP BY city
                   HAVING COUNT(*) > 1
                   """)

    for city2, count2 in cursor.fetchall():
        print(city2, count2)


def main():
    conn, cursor = create_database()

    try:
        create_tables(cursor)
        print("✅ INFO: Tables created successfully.")
        insert_data(cursor)
        print("✅ INFO: Data inserted successfully.")
        insert_tuple_data(cursor)
        print("✅INFO: Tuple Data inserted successfully.")
        select_operations(cursor)
        update_delete_operations(cursor)
        aggregate_functions(cursor)
        conn.commit()
    except sqlite3.Error as error:
        print(f"❌ ERROR: There was an error while creating tables: {error}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
