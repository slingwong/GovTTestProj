import sys

import mariadb


def before_all(context):
    print('Before all executed')
    test_teardown_function()


def create_db_connection():
    try:
        conn = mariadb.connect(
            user="user",
            password="userpassword",
            host="127.0.0.1",
            port=3306,
            database='testdb'
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None


def test_teardown_function():
    print("performing teardown")
    conn = create_db_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM working_class_heroes WHERE natid LIKE 'natid-%' AND (CAST(SUBSTR(natid, 7) AS SIGNED) <= 0 OR CAST(SUBSTR(natid, 7) AS SIGNED) >= 11)")
    conn.commit()
    conn.close()


def count_records():
    conn = create_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM working_class_heroes")
    count = cur.fetchone()[0]
    conn.close()
    return count
