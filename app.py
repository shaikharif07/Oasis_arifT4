from nltk.stem.snowball import stopwords
import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# data/text peprocessing

def transform_sms(sms):
    sms = sms.lower()
    sms = nltk.word_tokenize(sms)
    y = []
    for i in sms:
        if i.isalnum():
            y.append(i)

    # sms = y (error since y is a list)
    sms = y[:]
    y.clear()

    for i in sms:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    sms = y[:]
    y.clear()

    for i in sms:
        y.append(ps.stem(i))

    return " ".join(y)


tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Oasis Task 4- Email spam Classifier")
inp_sms = st.text_input("Enter the msg to check if spam or not: ")

# button
if st.button("Predict"):

    # transform function
    tran_sms = transform_sms(inp_sms)

    # vectorize
    vector_inp = tfidf.transform([tran_sms])

    # predict
    result = model.predict(vector_inp)[0]

    # display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not a spam")
