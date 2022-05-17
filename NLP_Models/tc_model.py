import pandas as pd
import numpy as np
import re, string
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import SnowballStemmer
# from nltk.corpus import wordnet
# from nltk.stem import WordNetLemmatizer

df = pd.read_excel("./Scrapper_New/Data_Files/Final/CrimevsNonCrime.xlsx")
df['label']
print(df)