# News-article-sentiment-and-emotion-analysis
This Python-based project performs sentiment and emotion analysis on news articles fetched from the web. 

The project processes the article's text, **extracts emotions using the NRC Emotion Lexicon, performs sentiment analysis using VADER, and visualizes the emotion distribution through a bar chart**. 

The goal is to gain insights into the **emotional tone of news articles and understand their overall sentiment**.

#**Features**

1)**Fetch News Articles**: Retrieves a news article's content from a given URL using web scraping techniques with requests and BeautifulSoup.

2)**Text Cleaning and Preprocessing**: Cleans the fetched text by converting it to lowercase, removing punctuation, and tokenizing it.

3)**Stop Word Removal**: Removes common stop words (e.g., "the", "and", "is") that do not add significant meaning to the text.

4)**Lemmatization**: Standardizes words to their base or root form, ensuring consistency in word representation (e.g., "running" becomes "run").

5)**Emotion Extraction**: Uses the NRC Emotion Lexicon via the NRCLex library to identify the most dominant emotions associated with words in the article.

6)**Sentiment Analysis**: Utilizes the VADER sentiment analysis tool to classify the sentiment of the article as Positive, Negative, or Neutral based on the 
overall emotional tone.

7)**Emotion Distribution Visualization**: Plots a bar chart that visually represents the distribution of emotions in the article using matplotlib.

8)**Error Handling**: Includes error handling for failed HTTP requests when fetching articles, with informative messages to guide the user.


#**Output**

1)**Fetched Article Text**: Displays a snippet of the fetched article (first 500 characters).

2)**Emotion Analysis**: Prints the dominant emotions and their frequencies.

3)**Sentiment Analysis**: Provides the overall sentiment classification (Positive, Negative, or Neutral).

4)**Emotion Distribution Bar Chart**: Displays a bar chart of the emotion frequencies.


#**Enhancements Added**

1)**HTTP Request Error Handling**: Checks for response status and provides informative error messages for failed HTTP requests.

2)**Detailed Sentiment Scoring**: Displays the compound score for sentiment analysis, offering additional insight into the sentiment classification.

3)**Emotion Detection Check**: Ensures the script does not attempt to plot a chart if no emotions are detected.


#**Main Functions**

1)**fetch_news_article(url)**

->Fetches and returns the text of the article from the provided URL.

->Uses the requests library to send an HTTP GET request.

->Parses the HTML content of the page with BeautifulSoup to extract all paragraph text.

2)**clean_text(text)**

->Converts the input text to lowercase.

->Removes punctuation using Python's built-in string.punctuation to ensure clean tokenization and analysis.

3)**tokenization(cleaned_text)**

->Tokenizes the cleaned text into individual words using the word_tokenize function from NLTK.

->Tokenization splits the text into smaller units (tokens) like words or punctuation, which can be analyzed further.

4)**remove_stopwords(tokenized_words)**

->Removes common stop words from the tokenized words using NLTK's predefined stopwords list for the English language.

->This step helps eliminate irrelevant words that do not contribute to the meaning of the text.

5)**lemmatize_words(final_words)**

->Lemmatizes the tokenized words using NLTK's WordNetLemmatizer, which reduces words to their base form (e.g., "better" becomes "good").

->Lemmatization ensures that similar words in different forms are treated as the same word.

6)**extract_emotions_nrc(words)**

->Analyzes each word for emotions using the NRCLex library, which maps words to emotions from the NRC Emotion Lexicon.

->Extracts the dominant emotion for each word and returns a frequency count of emotions in the article.

7)**analyze_sentiment(text)**

->Performs sentiment analysis on the entire article using VADER (Valence Aware Dictionary and sEntiment Reasoner).

->The sentiment score is calculated based on a composite score that reflects the article's overall sentiment (Positive, Negative, or Neutral).

8)**plot_emotions(emotion_counts)**

->Plots a bar chart that visualizes the frequency of different emotions in the article.

->Uses matplotlib to generate a bar chart showing the relative distribution of emotions such as joy, sadness, anger, etc.



#**Notes**

1)**Emotion Detection**: If no emotions are detected, the script skips chart plotting and informs the user.

2)**VADER Sentiment Scoring**: Provides detailed sentiment scores, including a compound score reflecting the overall sentiment polarity.

3)**NRC Emotion Lexicon**: Analyzes predefined emotions such as "joy," "anger," "fear," and "sadness."



#**Disclaimer**

<span style="font-size: 20px; font-weight: bold;">Disclaimer</span>

This code is purely for educational purpose only.
