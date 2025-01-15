from collections import defaultdict


def build_inverted_index(docs):
    inverted_index = defaultdict(list)
    for doc_id, doc in enumerate(docs):
        for term in set(doc.split()):
            inverted_index[term].append(doc_id)
    return inverted_index
