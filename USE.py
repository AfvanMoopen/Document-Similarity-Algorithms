import tensorflow_hub as hub

def process_use_similarity():
	filename = "./models/universal-sentence-encoder_4"
	model = hub.load(filename)

	base_embeddings = model([base_document])

	embeddings = model(documents)

	scores = cosine_similarity(base_embeddings, embeddings).flatten()
