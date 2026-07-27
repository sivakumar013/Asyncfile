import time
from bs4 import BeautifulSoup


def read_html(file_path):
    try:
        time.sleep(1)

        with open(file_path, "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs:
            text += p.get_text() + "\n"

        return {
            "title": title,
            "content": text
        }

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return {}

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return {}

    except Exception as e:
        print(f"Unexpected error reading HTML file: {e}")
        return {}


if __name__ == "__main__":
    page = read_html("../data/html/index.html")

    print("===== HTML FILE =====")

    if page:
        print(page)
    else:
        print("No HTML data available.")