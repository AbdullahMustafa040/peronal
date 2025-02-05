import pandas as pd

class ChtgptRomanUrduStopwords:
    def __init__(self, csv_path):
        self.stopwords = set(self.load_stopwords(csv_path))
    
    def load_stopwords(self, csv_path):
        df = pd.read_csv(csv_path, header=None)  # Load CSV with no column names
        return df.iloc[:, 0].tolist()  # Extract the first column as stopwords list
    
    def remove_stopwords(self, sentence: str) -> str:
        words = sentence.split()
        filtered_words = [word for word in words if word.lower() not in self.stopwords]
        return " ".join(filtered_words)