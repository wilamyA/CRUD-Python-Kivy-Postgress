from conn import conecta_db

conn = conecta_db()


def inserir_dados(name, age):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO person (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()


def ler_dados():
    cur = conn.cursor()
    cur.execute("SELECT nome, idade FROM person")
    person = cur.fetchall()
    cur.close()
    return person
