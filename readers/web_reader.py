import requests
from bs4 import BeautifulSoup
import time


def read_webpage(url):
    try:
        time.sleep(1)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"

        paragraphs = soup.find_all("p")

        text = ""

        for p in paragraphs[:3]:
            text += p.get_text() + "\n"

        return {
            "title": title,
            "content": text
        }

    except requests.exceptions.Timeout:
        print(f"Error: Request timed out for {url}")
        return {}

    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {url}")
        return {}

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error for {url}: {e}")
        return {}

    except requests.exceptions.RequestException as e:
        print(f"Request Error for {url}: {e}")
        return {}

    except Exception as e:
        print(f"Unexpected error reading webpage: {e}")
        return {}


if __name__ == "__main__":
    page1 = read_webpage("https://www.indmoney.com/")
    page2 = read_webpage("https://www.python.org/")

    print("===== PAGE 1 =====")
    if page1:
        print(page1)
    else:
        print("No webpage data available.")

    print("\n===== PAGE 2 =====")
    if page2:
        print(page2)
    else:
        print("No webpage data available.")