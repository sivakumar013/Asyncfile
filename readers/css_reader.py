import time


def read_css(file_path):
    try:
        time.sleep(1)

        with open(file_path, "r", encoding="utf-8") as file:
            css = file.read()

        return css

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return ""

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return ""

    except Exception as e:
        print(f"Unexpected error reading CSS file: {e}")
        return ""


if __name__ == "__main__":
    style = read_css("../data/css/style.css")

    print("===== CSS FILE =====")

    if style:
        print(style)
    else:
        print("No CSS content available.")