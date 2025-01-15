import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()


def preprocess(text):
    tokens = re.findall(r"\b\w+\b", text.lower())
    return " ".join(stemmer.stem(word) for word in tokens if word not in stop_words)
