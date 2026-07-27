import json
import time


def reader_json(file_path):
    try:
        time.sleep(1)

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return []

    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format - {file_path}")
        return []

    except Exception as e:
        print(f"Unexpected error reading JSON file: {e}")
        return []


if __name__ == "__main__":
    json_data = reader_json("../data/json/employees.json")

    print("===== JSON FILE =====")

    if json_data:
        for employee in json_data:
            print(employee)
    else:
        print("No JSON data available.")