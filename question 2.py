# SQLite is a lightweight database system that can be used
# directly from Python without requiring a separate database
# server.
#
# The sqlite3 module provides the functionality required to
# work with SQLite databases.
#
# The sqlite3.connect() function is used to establish a
# connection to an SQLite database.
#
# If the specified database file does not already exist,
# SQLite creates it.
#
# A cursor object is used to execute SQL statements against
# the database.
#
# The cursor allows Python to send SQL commands such as
# CREATE, INSERT, UPDATE and SELECT to the database.
#
# The commit() method saves changes made to the database.
# Without committing changes, modifications such as INSERT
# and UPDATE operations may not be permanently saved.
#
# The connection should be closed after database operations
# have been completed.

import sqlite3


# Connect to the SQLite database
connection = sqlite3.connect("students.db")

# Create a cursor object
cursor = connection.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course TEXT NOT NULL
    )
""")

# Insert data into the table
cursor.execute("""
    INSERT INTO students (name, course)
    VALUES (?, ?)
""", ("Tinotenda", "Information Technology"))

# Save the changes to the database
connection.commit()

# Retrieve the records from the database
cursor.execute("SELECT * FROM students")

# Store the returned records
students = cursor.fetchall()

# Display the records
print("Students:")
for student in students:
    print(student)

# Close the database connection
connection.close()

