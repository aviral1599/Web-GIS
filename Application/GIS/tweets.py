import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests

def tweet():
    # url = 'http://127.0.0.1:3000/total'
    # r = requests.get(url)
    # df = pd.read_json(r.text)
    # print(df)
    
    df2 = pd.read_excel(r"realtime.xlsx")
    print(df2)
    n1 = df2.shape[0]
    m1 = df2.shape[1]
    col2 = df2.columns
    data2 = []
    text = []
    crime = []
    location = []
    temp = {}
    for i in range(n1):
        text.append(df2.iloc[i][1])
        crime.append(df2.iloc[i][4])
        location.append(df2.iloc[i][5])
    
    data2.append(text)
    data2.append(crime)
    data2.append(location)
    
    return data2