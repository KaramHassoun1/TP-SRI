from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess


def process_query(query, vectorizer):
    query_tokens = preprocess(query)
    return vectorizer.transform([query_tokens])


def rank_documents(query_vector, tfidf_matrix):
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
    ranked_doc_indices = similarity_scores.argsort()[::-1]
    return ranked_doc_indices, similarity_scores
