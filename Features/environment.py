import mariadb

def before_all(context):
    print('Before all executed')
    test_teardown_function()


def test_teardown_function():
    print("performing teardown")
    try:
        conn = mariadb.connect(
            user="user",
            password="userpassword",
            host="127.0.0.1",
            port=3306,
            database='testdb'
        )
    except mariadb.Error as e:
        print("error connecting to mariadb")
        print(e)
        sys.exit(1)

    cur = conn.cursor()

    cur.execute(
        "DELETE FROM working_class_heroes WHERE natid LIKE 'natid-%' AND (CAST(SUBSTR(natid, 7) AS SIGNED) <= 0 OR CAST(SUBSTR(natid, 7) AS SIGNED) >= 11)")
    conn.commit()
    conn.close()
