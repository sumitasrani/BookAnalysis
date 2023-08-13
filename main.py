import re
import streamlit as st
import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px


st.title("Book Analysis")

with open(".ipynb_checkpoints/miracle_in_the_andes-checkpoint.txt", "r") as file:
    book = file.read()

# Total no.of chapters
pattern = re.compile("Chapter [0-9]+")
no_chap = re.findall(pattern, book)

# Number of sentences with the word: love
pattern_word = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
sent_count = re.findall(pattern_word, book)

# Count most used words

# Total occurrence of each word

# First occurrence of each word
occur = re.compile("[a-zA-Z]+")
find_occur = re.findall(occur, book.lower())

# Total occurrence of each word
word_occur = {}
for word in find_occur:
    if word in word_occur.keys():
        word_occur[word] = word_occur[word] + 1
    else:
        word_occur[word] = 1

# sorting word list
list_new = [(value, key) for (key, value) in word_occur.items()]
sorted_list = sorted(list_new, reverse=True)

# Remove stop words
english_stopwords = stopwords.words("english")
filtered_list = []
for count, word in sorted_list:
    if word not in english_stopwords:
        filtered_list.append((word, count))


st.info("Text Analysis of the Book")
st.write(f"Total no: of Chapters in the Book: {len(no_chap)}")
st.write(f"No. Sentences with the word love: {len(sent_count)}")


# Sentiment Analysis with polarity
analyzer = SentimentIntensityAnalyzer()
total_chap = re.compile("Chapter [0-9]+")
chapters = re.split(total_chap, book)
chapters = chapters[1:]

for nr, chapter in enumerate(chapters):
    score = analyzer.polarity_scores(chapter)
    st.info(f"Score for each chapter {score}")
    # figure = px.line(x=score, y=chapter, labels={"x": "Dates", "y": "Temperature (deg C)"})
   # st.plotly_chart(figure)

