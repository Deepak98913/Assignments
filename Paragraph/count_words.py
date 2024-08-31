import string
from collections import Counter

def count_words(file_path):
    """Read a file, count the occurrences of each word, and display results in alphabetical order.

    Args:
        file_path (str): Path to the file containing the text.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            
            # Normalize text: convert to lowercase and remove punctuation
            text = text.lower()
            text = text.translate(str.maketrans('', '', string.punctuation))
            
            # Split the text into words
            words = text.split()
            
            # Count word occurrences
            word_count = Counter(words)
            
            # Display results in alphabetical order
            for word in sorted(word_count.keys()):
                print(f"{word}: {word_count[word]}")
                
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

# File path
file_path = 'paragraph.txt'

# Count words and display results
count_words(file_path)
