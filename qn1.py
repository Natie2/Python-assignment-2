"""Question 1: Connect to SQLite, create a table, insert data, retrieve data."""

import sqlite3


def main():
    # 1. Connect (the file is created automatically if it does not exist)
    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    try:
        # 2. Create the table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                name    TEXT    NOT NULL,
                course  TEXT    NOT NULL,
                mark    REAL
            )
        """)

        # 3. Insert data (parameterised - never use string formatting)
        cursor.execute("DELETE FROM students")  # keep re-runs clean
        cursor.execute(
            "INSERT INTO students (name, course, mark) VALUES (?, ?, ?)",
            ("Tanatswa Mugandani", "Python Programming", 72.5),
        )
        cursor.executemany(
            "INSERT INTO students (name, course, mark) VALUES (?, ?, ?)",
            [
                ("Estacy Tanganyika", "Database Systems", 60.0),
                ("Cindy Chikuni", "Python Programming", 85.0),
                ("Sheila James", "Networks", 55.5),
            ],
        )
        connection.commit()

        # 4. Retrieve the data
        cursor.execute("SELECT id, name, course, mark FROM students ORDER BY mark DESC")
        rows = cursor.fetchall()

        print(f"{'ID':<4}{'Name':<18}{'Course':<22}{'Mark':>6}")
        print("-" * 50)
        for row in rows:
            print(f"{row[0]:<4}{row[1]:<18}{row[2]:<22}{row[3]:>6.1f}")
        print(f"\n{len(rows)} record(s) retrieved.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        # 5. Always close the connection
        connection.close()


if __name__ == "__main__":
    main()
