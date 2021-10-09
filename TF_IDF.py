from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def process_tfidf_similarity():
	vectorizer = TfidfVectorizer()

	# To make uniformed vectors, both documents need to be combined first.
	documents.insert(0, base_document)
	embeddings = vectorizer.fit_transform(documents)

	cosine_similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()
