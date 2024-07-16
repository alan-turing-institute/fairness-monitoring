import pandas as pd
import random
import nltk
import re
nltk.download('punkt')

def load_vocabulary_from_csv(csv_path, target_column):
    """
    Load vocabulary from a CSV file.
    The CSV should have a column for target words.
    """
    df = pd.read_csv(csv_path)
    vocabulary = df[target_column].tolist()
    return vocabulary

def split_alpha_numeric(tokens):
    split_tokens = []
    for token in tokens:
        # Split the token into alphabetic and numeric parts
        parts = re.findall(r'[A-Za-z]+|\d+', token)
        split_tokens.extend(parts)
    return split_tokens

def generate_random_counterfactual(sentence, vocab_path, target_column):
    """
    Generate counterfactual text by replacing target words with random words from the same vocabulary.
    """
    vocabulary = load_vocabulary_from_csv(vocab_path, target_column)
    vocabulary = [str(word).lower() for word in vocabulary]

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    words = split_alpha_numeric(nltk.word_tokenize(sentence))
    counterfactual_words = []

    if len(words) == 0:
        return sentence

    for word in words:
        if word.lower() in vocabulary:
            replacement = random.choice(vocabulary)
            while replacement == word.lower():
                replacement = random.choice(vocabulary)
            counterfactual_words.append(replacement)
        else:
            counterfactual_words.append(word)

    return ' '.join(counterfactual_words)


def generate_counterfactuals(sentence, vocab_path, target_column):
    """
    Generate counterfactual text by replacing target words with random words from the same vocabulary.
    """
    vocabulary = load_vocabulary_from_csv(vocab_path, target_column)
    vocabulary = [str(word).lower() for word in vocabulary]

    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    words = split_alpha_numeric(nltk.word_tokenize(sentence))
    
    counterfactual_sentences = []

    if len(words) == 0:
        return sentence
    
    for candidate in vocabulary:
        counterfactual_words = []
        for word in words:
            if word.lower() in vocabulary:
                counterfactual_words.append(candidate)
            else:
                counterfactual_words.append(word)

        counterfactual_sentences.append(' '.join(counterfactual_words))
    
    return counterfactual_sentences