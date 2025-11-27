import os
import subprocess

def compress_pdf(input_pdf, output_pdf, quality="screen"):
    """
    Compress a PDF using Ghostscript.
    quality options: screen, ebook, printer, prepress
    """

    gs_command = "gswin64c" if os.name == "nt" else "gs"

    cmd = [
        gs_command,
        "-sDEVICE=pdfwrite",
        f"-dPDFSETTINGS=/{quality}",
        "-dCompatibilityLevel=1.4",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_pdf}",
        input_pdf,
    ]

    subprocess.run(cmd, check=True)


def compress_folder(input_folder, output_folder, quality="screen"):
    """
    Compress all PDFs in a folder.
    """

    if not os.path.isdir(input_folder):
        print("❌ Input folder not found.")
        return

    os.makedirs(output_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the folder.")
        return

    print(f"\n=== Compressing {len(pdf_files)} PDF files ===\n")

    for pdf in pdf_files:
        input_path = os.path.join(input_folder, pdf)
        output_path = os.path.join(output_folder, pdf)

        print(f"➡ Compressing: {pdf} ...")

        try:
            compress_pdf(input_path, output_path, quality)
            print(f"   ✓ Done → {output_path}")
        except Exception as e:
            print(f"   ❌ Failed: {e}")

    print("\n🎉 All done!")


if __name__ == "__main__":
    print("=== Batch PDF Compressor (Ghostscript) ===")

    input_folder = input("Enter the input folder path: ").strip()
    output_folder = input("Enter the output folder path: ").strip()
    quality = input("Choose quality (screen, ebook, printer, prepress) [default: screen]: ").strip()

    if not quality:
        quality = "screen"

    compress_folder(input_folder, output_folder, quality)