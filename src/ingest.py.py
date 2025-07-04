from pathlib import Path
import fitz  # PyMuPDF
def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF using PyMuPDF """
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
        print(f"[✓] Extracted: {pdf_path.name}")
    except Exception as e:
        print(f"[x] Error reading {pdf_path.name}: {e}")
    return text

def load_all_pdfs(input_folder="data/", output_file="data/combined_text.txt"):
    """Combine text from all PDFs in folder into a single .txt file"""
    folder = Path(input_folder)
    pdf_files = sorted(folder.glob("*.pdf"))
    if not pdf_files:
        print("⚠️  No PDF files found in folder!")
        return
    combined_text = ""
    for pdf in pdf_files:
        combined_text += f"\n\n--- {pdf.name} ---\n\n"
        combined_text += extract_text_from_pdf(pdf).strip() + "\n"

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(combined_text)
    print(f"\n[✓] All PDFs combined and saved to: {output_file}")

if __name__ == "__main__":
    load_all_pdfs()

