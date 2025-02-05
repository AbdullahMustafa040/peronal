import json

class HaseebElahiRomanUrduStopwords:
    def __init__(self):
        """
        Initialize the class with the list of Roman Urdu stop words.
        """
        self.stop_words = self._load_stop_words()

    def _load_stop_words(self):
        """
        Load the stop words from the provided JSON string.
        """
        stop_words_json = '''
        {
            "roman_urdu_stop_words": [
                "ai", "ayi", "hy", "hai", "main", "ki", "tha", "koi", "ko", "sy", "woh", 
                "bhi", "aur", "wo", "yeh", "rha", "hota", "ho", "ga", "ka", "le", "lye", 
                "kr", "kar", "lye", "liye", "hotay", "waisay", "gya", "gaya", "kch", "ab",
                "thy", "thay", "houn", "hain", "han", "to", "is", "hi", "jo", "kya", "thi",
                "se", "pe", "phr", "wala", "waisay", "us", "na", "ny", "hun", "rha", "raha",
                "ja", "rahay", "abi", "uski", "ne", "haan", "acha", "nai", "sent", "photo", 
                "you", "kafi", "gai", "rhy", "kuch", "jata", "aye", "ya", "dono", "hoa", 
                "aese", "de", "wohi", "jati", "jb", "krta", "lg", "rahi", "hui", "karna", 
                "krna", "gi", "hova", "yehi", "jana", "jye", "chal", "mil", "tu", "hum", "par", 
                "hay", "kis", "sb", "gy", "dain", "krny", "tou"
            ]
        }
        '''
        stop_words_data = json.loads(stop_words_json)
        return set(stop_words_data["roman_urdu_stop_words"])

    def remove_stop_words(self, sentence):
        """
        Remove stop words from the given sentence.

        Args:
            sentence (str): The input sentence.

        Returns:
            str: The sentence without stop words.
        """
        # Split the sentence into words
        words = sentence.split()

        # Remove stop words
        filtered_words = [word for word in words if word.lower() not in self.stop_words]

        # Join the filtered words back into a sentence
        return " ".join(filtered_words)