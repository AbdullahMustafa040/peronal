from openai import OpenAI

class OpenAIGPTEmbedding:
    def __init__(self, model="text-embedding-ada-002", api_key=None):
        self.model = model
        print(api_key)
        self.client = OpenAI(api_key=api_key)

    def get_embedding(self, sentence):
        """
        Gets the embedding for a given sentence.

        Args:
            sentence: The sentence to get the embedding for.

        Returns:
            The embedding for the sentence.
        """
        response = self.client.embeddings.create(
            input=sentence,
            model=self.model
        )
        return response.data[0].embedding
