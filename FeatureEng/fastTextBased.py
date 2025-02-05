import fasttext

class FastTextEmbedding:
    def __init__(self, model_path):
        self.model = fasttext.load_model(model_path)

    def get_embedding(self, sentence):
        # fastText provides a get_sentence_vector method
        return self.model.get_sentence_vector(sentence)
