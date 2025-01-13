import string
import matplotlib.pyplot as plt

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nrclex import NRCLex
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter

import requests #Used to make important request such as GET
from bs4 import BeautifulSoup


# Function to fetch news articles
def fetch_news_article(url):
    """
    Fetches text from a news article URL using requests and BeautifulSoup.
    """
    response = requests.get(url) #Sends an HTTP GET request

    if response.status_code != 200:
        print(f"Failed to fetch the article. HTTP Status Code: {response.status_code}") #Requests failure
        exit()
    
    soup = BeautifulSoup(response.content, 'html.parser') 
    paragraphs = soup.find_all('p') #Finds all the <p> tags in the HTML
    article_text = ' '.join([para.get_text() for para in paragraphs]) #Concatenates the text of all the para into single string
    return article_text


def clean_text(text): 
 """
Converts text to lower case and remove punctuation marks
 """
 lower_case = text.lower() #To lower case
 cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation)) #Removing of punctuation marks
 return cleaned_text


def tokenization(cleaned_text):
 """
 Tokenization
 """
 return word_tokenize(cleaned_text, "english")


def remove_stopwords(tokenized_words): 
 """
 Removing Stop Words
 """
 final_words = []
 for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
 return final_words


def lemmatize_words(final_words):
  """
  Lemmatization of the words
  """
  lemma_words = []
  for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
  return lemma_words


def extract_emotions_nrc(words):
    """
    Uses the NRCLex library to extract emotions from words and returns a Counter of emotion frequencies.
    """
    emotion_list = []
    for word in words:
        nrc = NRCLex(word) 
        if nrc.raw_emotion_scores: #nrc.raw_emotion_scores is a dictionary containing emotions as keys
            # Extract the most dominant emotion for the word
            top_emotion = max(nrc.raw_emotion_scores, key=nrc.raw_emotion_scores.get)
            emotion_list.append(top_emotion)
    return Counter(emotion_list)


# Function to perform sentiment analysis using VADER
def analyze_sentiment(text):
    """
    Analyzes sentiment using VADER and returns the overall sentiment.
    """
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    print("Score for the sentiment analysis is: ",score['compound'])
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

'''
The score['compound'] in VADER sentiment analysis is a single, normalized metric that represents the overall sentiment polarity of a given text.
It is calculated as a weighted sum of the individual word sentiment scores, normalized to range between -1 (most negative) and 1 (most positive).
'''


# Function to plot emotion distribution
def plot_emotions(emotion_counts):
    """
    Plots a bar chart of emotion frequencies.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(emotion_counts.keys(), emotion_counts.values(), color='skyblue')
    plt.title("Emotion Distribution")
    plt.xlabel("Emotions")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()


# Input: URL of a news article
url = input("Enter the URL of a news article: ")
article = fetch_news_article(url)
print("\nFetched Article Text:\n", article[:500], "...")  # Displaying first 500 characters


cleaned_text = clean_text(article)
tokenized_words= tokenization(cleaned_text)
final_words= remove_stopwords(tokenized_words)
lemma_words= lemmatize_words(final_words)


# Emotion Analysis
emotions = extract_emotions_nrc(lemma_words)
print("\nEmotion Analysis:\n", emotions)


# Sentiment Analysis
sentiment = analyze_sentiment(article)
print("\nSentiment Analysis: The article is", sentiment)


# Plotting Emotion Distribution
if emotions: #Checking whether are any emotions to plot or not
    plot_emotions(emotions)
else:
   print("No emotions detected to plot.")