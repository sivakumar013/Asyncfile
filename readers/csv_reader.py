import pandas as pd
import time


def read_csv(file_path):
    try:
        time.sleep(1)

        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return pd.DataFrame()

    except pd.errors.EmptyDataError:
        print(f"Error: CSV file is empty - {file_path}")
        return pd.DataFrame()

    except pd.errors.ParserError:
        print(f"Error: Unable to parse CSV file - {file_path}")
        return pd.DataFrame()

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return pd.DataFrame()

    except Exception as e:
        print(f"Unexpected error reading CSV file: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    sales = read_csv("data/csv/sales.csv")
    customers = read_csv("data/csv/customers.csv")

    print("===== SALES =====")
    if not sales.empty:
        print(sales)
    else:
        print("No sales data available.")

    print("\n===== CUSTOMERS =====")
    if not customers.empty:
        print(customers)
    else:
        print("No customer data available.")