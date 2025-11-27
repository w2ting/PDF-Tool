import PyPDF2
import os

def merge_all_pdfs_in_folder():
    folder = input("Enter the folder path containing PDF files: ").strip()

    if not os.path.isdir(folder):
        print("Invalid folder path.")
        return

    # Collect all PDFs in the folder
    pdf_files = [f for f in os.listdir(folder) if f.lower().endswith(".pdf")]
    pdf_files.sort()  # Optional: merge in alphabetical order

    if not pdf_files:
        print("No PDF files found in the folder.")
        return

    output_pdf = input("Enter the output PDF name (e.g., merged.pdf): ").strip()

    merger = PyPDF2.PdfMerger()

    print("\nMerging the following files:")
    for pdf in pdf_files:
        print(f" - {pdf}")
        merger.append(os.path.join(folder, pdf))

    merger.write(output_pdf)
    merger.close()

    print(f"\n✅ Successfully merged {len(pdf_files)} PDFs into: {output_pdf}")


if __name__ == "__main__":
    merge_all_pdfs_in_folder()