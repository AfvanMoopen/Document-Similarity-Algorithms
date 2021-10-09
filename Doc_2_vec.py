from gensim.models.doc2vec import Doc2Vec

def process_doc2vec_similarity():

	filename = './models/enwiki_dbow/doc2vec.bin'
	model= Doc2Vec.load(filename)

	tokens = preprocess(base_document)

	# Only handle words that appear in the doc2vec pretrained vectors. enwiki_ebow model contains 669549 vocabulary size.
	tokens = list(filter(lambda x: x in model.wv.vocab.keys(), tokens))
	base_vector = model.infer_vector(tokens)
