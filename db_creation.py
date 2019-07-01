import sqlite3

connection = sqlite3.connect('db/student_details.db')

cursor = connection.cursor()

sql = """CREATE TABLE student_details (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Marks INT NOT NULL,
    Roll INT NOT NULL
)"""
# sql = """INSERT INTO login(userid, password) VALUES ('ayan', )"""
cursor.execute(sql)


print("DATABASE created successfully")
connection.commit()