import openai
import numpy as np

class OpenAIGPTEmbedding:
    def __init__(self, api_key, model='text-embedding-ada-002'):
        openai.api_key = api_key
        self.model = model

    def get_embedding(self, sentence):
        response = openai.Embedding.create(
            input=sentence,
            model=self.model
        )
        embedding = response['data'][0]['embedding']
        return np.array(embedding)
