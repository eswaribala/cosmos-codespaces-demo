import psycopg

HOST = "localhost"
PORT = 9712
DBNAME = "postgres"
USER = "cosmosdev"
PASSWORD = ""  # trust auth in your current setup

conn = psycopg.connect(
    host=HOST,
    port=PORT,
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    sslmode="require",
)

with conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                name TEXT NOT NULL,
                age INT
            )
        """)

        cur.execute("""
            INSERT INTO users (id, user_id, name, age)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE
            SET user_id = EXCLUDED.user_id,
                name = EXCLUDED.name,
                age = EXCLUDED.age
        """, ("1", "u1", "Bala", 30))

        cur.execute("""
            INSERT INTO users (id, user_id, name, age)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE
            SET user_id = EXCLUDED.user_id,
                name = EXCLUDED.name,
                age = EXCLUDED.age
        """, ("2", "u2", "John", 28))

        cur.execute("SELECT id, user_id, name, age FROM users ORDER BY id")
        rows = cur.fetchall()

print("Items in table:")
for row in rows:
    print({
        "id": row[0],
        "userId": row[1],
        "name": row[2],
        "age": row[3],
    })