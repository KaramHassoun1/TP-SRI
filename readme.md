# Function Descriptions

## 1. `preprocess(text)`
**Purpose:**  
Prepares raw text data by cleaning and normalizing it for analysis.

### What it does:
- **Tokenization:** Splits the input text into individual words (tokens).  
- **Lowercasing:** Converts all tokens to lowercase to make comparisons case-insensitive.  
- **Stop Word Removal:** Removes common, uninformative words like "the," "and," or "is."  
- **Stemming:** Reduces words to their root form (e.g., "running" → "run").

---

## 2. `build_inverted_index(docs)`
**Purpose:**  
Creates an inverted index for efficient document retrieval.

### What it does:
- Iterates over each document in the preprocessed collection.  
- For each term in a document, adds the document ID to the list of documents containing that term.

---

## 3. `compute_tfidf(documents)`
**Purpose:**  
Transforms the document collection into a TF-IDF matrix for vector representation.

### What it does:
- **Computes Term Frequency (TF):** How often a term appears in a document.  
- **Computes Inverse Document Frequency (IDF):** How unique a term is across all documents.  
- Combines these scores to produce the TF-IDF value for each term in each document.

---

## 4. `process_query(query, vectorizer)`
**Purpose:**  
Converts a user query into a vector compatible with the TF-IDF matrix.

### What it does:
- Preprocesses the query text (same steps as the `preprocess` function).  
- Uses the TF-IDF vectorizer to transform the preprocessed query into a vector.

---

## 5. `rank_documents(query_vector, tfidf_matrix)`
**Purpose:**  
Calculates similarity between the query and documents and ranks them.

### What it does:
- **Computes Cosine Similarity:** Measures how similar two vectors are.  
  - Cosine similarity ranges from 0 (no similarity) to 1 (exact match).  
- Ranks documents based on their similarity scores in descending order.
