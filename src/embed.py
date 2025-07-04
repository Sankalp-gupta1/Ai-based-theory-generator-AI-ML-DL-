from sentence_transformers import SentenceTransformer
import torch
import os

TEXT_FILE = "data/cleaned_text.txt"
EMBEDDINGS_FILE = "data/paragraph_embeddings.pt"
PARAGRAPH_FILE = "data/paragraphs.txt"
MODEL_NAME = "all-MiniLM-L6-v2"
SAVED_MODEL_PATH = "model/saved_model"  # Model will be saved here

def load_text_chunks(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    return paragraphs

def save_paragraphs(paragraphs):
    with open(PARAGRAPH_FILE, "w", encoding="utf-8") as f:
        for para in paragraphs:
            f.write(para + "\n\n")

def embed_and_save():
    print("[📦] Loading model...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("[📄] Reading and chunking text...")
    paragraphs = load_text_chunks(TEXT_FILE)
    save_paragraphs(paragraphs)  # store raw paragraphs
    
    print("[🧠] Embedding paragraphs...")
    embeddings = model.encode(paragraphs, convert_to_tensor=True, show_progress_bar=True)
    
    print(f"[💾] Saving embeddings to: {EMBEDDINGS_FILE}")
    torch.save(embeddings, EMBEDDINGS_FILE)

    # Save the model after embedding
    print(f"[💾] Saving model to: {SAVED_MODEL_PATH}")
    model.save(SAVED_MODEL_PATH)  # Save the model for future use

    print("[✅] Done!")

if __name__ == "__main__":
    embed_and_save()
