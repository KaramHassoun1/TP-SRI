import os
import re

from inverted_index import build_inverted_index
from preprocessing import preprocess
from query_engine import process_query, rank_documents
from tfidf_vectorizer import compute_tfidf

DOCUMENTS_PATH = "docs"
documents = []


def natural_sort_key(filename):
    return [
        int(text) if text.isdigit() else text.lower()
        for text in re.split(r"(\d+)", filename)
    ]


for filename in sorted(os.listdir(DOCUMENTS_PATH), key=natural_sort_key):
    if filename.endswith(".txt"):
        with open(
            os.path.join(DOCUMENTS_PATH, filename), "r", encoding="utf-8"
        ) as file:
            documents.append(file.read())
preprocessed_docs = [preprocess(doc) for doc in documents]
inverted_index = build_inverted_index(preprocessed_docs)
vectorizer, tfidf_matrix, terms = compute_tfidf(preprocessed_docs)

while True:
    query = input("\nEnter your query (or press Enter to exit): ").strip()
    if not query:
        print("Exiting the program. Goodbye!")
        break
    query_vector = process_query(query, vectorizer)
    ranked_docs, scores = rank_documents(query_vector, tfidf_matrix)
    print("\nTop-ranked documents:")
    for rank, idx in enumerate(ranked_docs[:10]):
        filename = sorted(os.listdir(DOCUMENTS_PATH), key=natural_sort_key)[idx]
        print(
            f"Rank {rank + 1}: Document {idx + 1} ({filename}), Score: {scores[idx]:.4f}"
        )
