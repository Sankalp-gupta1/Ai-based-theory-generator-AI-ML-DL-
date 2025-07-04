import re
RAW_TEXT = "data/combined_text.txt"
CLEAN_TEXT = "data/cleaned_text.txt"

def clean_text(text):
    # Basic cleanup
    text = re.sub(r'\n+', '\n', text)                         # Multiple newlines -> one
    text = re.sub(r'\s+', ' ', text)                          # Multiple spaces -> one
    text = re.sub(r'([.?!])\s+', r'\1\n\n', text)             # End of sentence -> paragraph
    text = text.strip()
    return text
def preprocess():
    print("[📄] Reading raw text...")
    with open(RAW_TEXT, "r", encoding="utf-8") as f:
        raw = f.read()
    print("[🧹] Cleaning and structuring text...")
    cleaned = clean_text(raw)
    print(f"[💾] Saving cleaned text to: {CLEAN_TEXT}")
    with open(CLEAN_TEXT, "w", encoding="utf-8") as f:
        f.write(cleaned)
    print("[✅] Preprocessing done!")

if __name__ == "__main__":
    preprocess()
