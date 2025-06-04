import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re

nltk.download('punkt_tab')
nltk.download('stopwords')

def summarize_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    freq_table = {}
    for word in words:
        word = re.sub(r'\W+', '', word)
        if word not in stop_words and word != '':
            freq_table[word] = freq_table.get(word, 0) + 1

    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            word = re.sub(r'\W+', '', word)
            if word in freq_table:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq_table[word]

    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    return ' '.join(summary_sentences)
