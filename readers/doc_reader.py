from docx import Document
import time


def read_docx(file_path):
    try:
        time.sleep(1)

        document = Document(file_path)

        text = []

        for para in document.paragraphs:
            text.append(para.text)

        return "\n".join(text)

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return ""

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return ""

    except Exception as e:
        print(f"Unexpected error reading DOCX file: {e}")
        return ""


if __name__ == "__main__":
    report = read_docx("data/docx/report.docx")
    meeting = read_docx("data/docx/meeting.docx")

    print("===== REPORT =====")
    if report:
        print(report)
    else:
        print("No report data available.")

    print("\n===== MEETING =====")
    if meeting:
        print(meeting)
    else:
        print("No meeting data available.")