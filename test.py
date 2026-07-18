import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="company_db",
    user="postgres",
    password="REMOVED_PASSWORD"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()