import psycopg2
import time
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def employees():
    time.sleep(1)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def products():
    time.sleep(1)
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


if __name__ == "__main__":

    print("Employees")
    for row in employees():
        print(row)

    print("Products")
    for row in products():
        print(row)