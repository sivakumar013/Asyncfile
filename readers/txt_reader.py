import time


def read_txt(file_path):
    try:
        time.sleep(1)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return ""

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return ""

    except UnicodeDecodeError:
        print(f"Error: Unable to decode text file - {file_path}")
        return ""

    except Exception as e:
        print(f"Unexpected error reading text file: {e}")
        return ""


if __name__ == "__main__":
    notes = read_txt("../data/txt/project_objectives.txt")

    print("===== TEXT FILE =====")

    if notes:
        print(notes)
    else:
        print("No text data available.")