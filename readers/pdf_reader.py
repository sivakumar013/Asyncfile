from PyPDF2 import PdfReader
import time


def read_pdf(file_path):
    try:
        time.sleep(1)

        reader = PdfReader(file_path)

        text = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text.append(page_text)

        return "\n".join(text)

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return ""

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return ""

    except Exception as e:
        print(f"Unexpected error reading PDF file: {e}")
        return ""


if __name__ == "__main__":
    invoice = read_pdf("data/pdf/invoice.pdf")
    manual = read_pdf("data/pdf/manual.pdf")

    print("===== INVOICE =====")
    if invoice:
        print(invoice)
    else:
        print("No invoice data available.")

    print("\n===== MANUAL =====")
    if manual:
        print(manual)
    else:
        print("No manual data available.")