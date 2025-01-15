from sklearn.feature_extraction.text import TfidfVectorizer


def compute_tfidf(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out()
    return vectorizer, tfidf_matrix, terms
