import PyPDF2
import os

def split_range():
    input_pdf = input("Enter the PDF file name: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return
    start_page = int(input("Start page: "))
    end_page = int(input("End page: "))
    output_pdf = input("Output file name: ").strip()

    with open(input_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()

        if start_page < 1 or end_page > len(reader.pages) or start_page > end_page:
            print("Invalid page range.")
            return

        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        with open(output_pdf, "wb") as out:
            writer.write(out)
    print(f"✅ Pages {start_page}-{end_page} saved to {output_pdf}")

def merge_pdfs():
    files = input("Enter PDF file names separated by commas: ").strip().split(",")
    files = [f.strip() for f in files if os.path.isfile(f.strip())]
    if not files:
        print("No valid files found.")
        return
    output_pdf = input("Output file name: ").strip()
    merger = PyPDF2.PdfMerger()
    for pdf in files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()
    print(f"✅ Merged into {output_pdf}")

def remove_pages():
    input_pdf = input("Enter the PDF file name: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return
    pages_to_remove = input("Enter pages to remove (comma-separated, 1-based): ")
    pages_to_remove = [int(p.strip()) for p in pages_to_remove.split(",")]
    output_pdf = input("Output file name: ").strip()

    with open(input_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()
        for i in range(len(reader.pages)):
            if (i + 1) not in pages_to_remove:
                writer.add_page(reader.pages[i])
        with open(output_pdf, "wb") as out:
            writer.write(out)
    print(f"✅ Removed pages {pages_to_remove} → {output_pdf}")

def rotate_pages():
    input_pdf = input("Enter the PDF file name: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return
    rotation = int(input("Rotation angle (90, 180, 270): "))
    output_pdf = input("Output file name: ").strip()

    with open(input_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            page.rotate(rotation)
            writer.add_page(page)
        with open(output_pdf, "wb") as out:
            writer.write(out)
    print(f"✅ Rotated all pages by {rotation}° → {output_pdf}")

def password_protect():
    input_pdf = input("Enter the PDF file name: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return
    password = input("Enter password: ").strip()
    output_pdf = input("Output file name: ").strip()

    with open(input_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        writer = PyPDF2.PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.encrypt(password)
        with open(output_pdf, "wb") as out:
            writer.write(out)
    print(f"✅ Password set for {output_pdf}")

def extract_text():
    input_pdf = input("Enter the PDF file name: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return
    with open(input_pdf, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for i, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            print(f"--- Page {i} ---\n{text}\n")

# Main menu
while True:
    print("\n=== PDF Toolkit ===")
    print("1. Split a specific page range")
    print("2. Merge multiple PDFs")
    print("3. Remove pages")
    print("4. Rotate pages")
    print("5. Password-protect a PDF")
    print("6. Extract text from a PDF")
    print("0. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        split_range()
    elif choice == "2":
        merge_pdfs()
    elif choice == "3":
        remove_pages()
    elif choice == "4":
        rotate_pages()
    elif choice == "5":
        password_protect()
    elif choice == "6":
        extract_text()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
