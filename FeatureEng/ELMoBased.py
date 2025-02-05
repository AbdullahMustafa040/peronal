from allennlp.commands.elmo import ElmoEmbedder
import numpy as np

class ELMoEmbedding:
    def __init__(self):
        self.elmo = ElmoEmbedder()

    def get_embedding(self, sentence):
        tokens = sentence.split()
        embeddings = self.elmo.embed_sentence(tokens)
        # Average the embeddings across all three layers and tokens
        return np.mean(embeddings, axis=(0, 1))
