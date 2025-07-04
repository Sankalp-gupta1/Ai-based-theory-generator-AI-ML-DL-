from sentence_transformers import SentenceTransformer, util
import torch
import os

TEXT_FILE = "data/cleaned_text.txt"
MODEL_PATH = "model/saved_model"  # Load model from here
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def load_text_chunks(file_path):
    """Load combined text and split into chunks (or paragraphs)"""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Split on double newlines or paragraph chunks
    paragraphs = [para.strip() for para in text.split('\n\n') if para.strip()]
    return paragraphs

def embed_texts(model, texts):
    """Embed list of texts"""
    return model.encode(texts, convert_to_tensor=True, show_progress_bar=True)

def answer_question(question, model, paragraphs, paragraph_embeddings, top_k=3):
    """Return top_k best matching paragraphs from the document"""
    question_embedding = model.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(question_embedding, paragraph_embeddings)[0]
    top_results = torch.topk(scores, k=top_k)

    answers = []
    for score, idx in zip(top_results.values, top_results.indices):
        answers.append((score.item(), paragraphs[idx]))

    return answers

def main():
    print("[🔍] Loading model and text...")
    model = SentenceTransformer(MODEL_PATH, device=DEVICE)  # Load from the saved model
    paragraphs = load_text_chunks(TEXT_FILE)
    paragraph_embeddings = embed_texts(model, paragraphs)

    while True:
        print("\n📥 Ask your question (or type 'exit'): ")
        query = input(">> ")

        if query.lower() in ['exit', 'quit']:
            break

        results = answer_question(query, model, paragraphs, paragraph_embeddings)
        print("\n🔎 Top Answers (Detailed):")
        for i, (score, answer) in enumerate(results, 1):
            print(f"\n#{i} (Score: {score:.4f}):\n{answer}")

if __name__ == "__main__":
    main()
