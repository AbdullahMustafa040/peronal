!pip install NLTK
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')
# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')

class RomanUrduTokenizer:
    def __init__(self):
        pass

    def tokenize(self, text):

        # Tokenize the text using NLTK's word_tokenize
        tokens = word_tokenize(text)
        return tokens

# Example usage
if __name__ == "__main__":
    # Example Roman Urdu sentence
    roman_urdu_sentence = "Yeh ek test sentence hai. Isme kuch special characters !@#$%^&*() hain."
    paragraph = "kuch nahi hota..meri ma ka hai ausman card unko 2 baar hard atek ayaa tha ilaaj ke liy pase nahi the doctor ny bola is card se sarkar pase nahi milte"

    # Create an instance of RomanUrduTokenizer
    tokenizer = RomanUrduTokenizer()

    # Tokenize the sentence
    tokens = tokenizer.tokenize(roman_urdu_sentence)
    #tokens = tokenizer.tokenize(paragraph)

    # Print the tokens
    print("Tokens:", tokens)
