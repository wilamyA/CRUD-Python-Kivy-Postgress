import psycopg2


def conecta_db():
    conn = psycopg2.connect(
        host="localhost",
        database="person",
        user="dbadmin",
        password="dbadmin123"
    )

    return conn
