import pandas as pd
import time


def read_excel(file_path):
    try:
        time.sleep(1)

        df = pd.read_excel(file_path)

        return df.to_dict(orient="records")

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return []

    except ValueError:
        print(f"Error: Invalid Excel file - {file_path}")
        return []

    except Exception as e:
        print(f"Unexpected error reading Excel file: {e}")
        return []


if __name__ == "__main__":
    excel_data = read_excel("../data/excel/employees.xlsx")

    print("===== EXCEL FILE =====")

    if excel_data:
        for row in excel_data:
            print(row)
    else:
        print("No Excel data available.")