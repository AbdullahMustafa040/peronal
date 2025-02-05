from transformers import BertModel, BertTokenizer
import torch

class BERTEmbedding:
    def __init__(self, model_name='bert-base-uncased'):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.model.eval()

    def get_embedding(self, sentence):
        inputs = self.tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        # Use the pooled output as the sentence embedding
        return outputs.pooler_output.squeeze().numpy()
