# Challenge: Emoji Translator
# Task: Create a Python program that translates a sentence into emojis. Each word in the sentence should be replaced with a corresponding emoji.
# Try to handle various edge cases and expand the set of supported emojis.


def emoji_translator(sentence):
    # Logic to convert a sentence into emojis.
    
    # Dictionary mapping words to emojis
    emoji_dict = {
        'Python': '🐍',
        'programming': '💻',
        'is': '➡️',
        'fun': '😃',
        # Feel free to expand this dictionary with more words and emojis. 
        # If you have a creative addition, collaborate by adding items and send a pull request on the GitHub repo.
        # The link to the repo is in the comment section below. Let's build a diverse set of emojis together!
    }

    # Split the sentence into words
    words = sentence.split()
    
    # Translate each word into emojis or keep the original word if not found in the dictionary
    translated_sentence = ' '.join(emoji_dict.get(word, word) for word in words)
    
    return translated_sentence


# Example
input_sentence = "programming"
output_sentence = emoji_translator(input_sentence)
print(output_sentence)