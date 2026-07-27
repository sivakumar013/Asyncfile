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
    conn = None
    cursor = None

    try:
        time.sleep(1)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()

        return data

    except psycopg2.Error as e:
        print(f"Database Error (employees): {e}")
        return []

    except Exception as e:
        print(f"Unexpected Error (employees): {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def products():
    conn = None
    cursor = None

    try:
        time.sleep(1)

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()

        return data

    except psycopg2.Error as e:
        print(f"Database Error (products): {e}")
        return []

    except Exception as e:
        print(f"Unexpected Error (products): {e}")
        return []

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":

    print("===== EMPLOYEES =====")
    employee_data = employees()

    if employee_data:
        for row in employee_data:
            print(row)
    else:
        print("No employee data available.")

    print("\n===== PRODUCTS =====")
    product_data = products()

    if product_data:
        for row in product_data:
            print(row)
    else:
        print("No product data available.")