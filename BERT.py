rom sentence_transformers import SentenceTransformer

def process_bert_similarity():
	# This will download and load the pretrained model offered by UKPLab.
	model = SentenceTransformer('bert-base-nli-mean-tokens')

	sentences = sent_tokenize(base_document)
	base_embeddings_sentences = model.encode(sentences)
	base_embeddings = np.mean(np.array(base_embeddings_sentences), axis=0)
