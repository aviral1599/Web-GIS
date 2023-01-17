from flask import Flask,render_template ,request
from GIS.map import plotting
# from GIS.tweets import tweet 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
 

sys.path.insert(0, 'NLP_Models')
from Test_model import predict_tweet

app = Flask(__name__)

@app.route("/")
def home():
    options = ['Murder','Theft','Rape','Kidnap','Total']
    selected = options[0]
    # # tweets = tweet()
    # desc = tweets[0]
    # crimetype = tweets[1]
    # location = tweets[2]
    return render_template("home.html",name = 'new_plot', url ='static\images\india.png',options = options,selected=selected)

@app.route("/map",methods=['GET', 'POST'])
def map():
    crime = list(request.form.values())
    
    p = plotting()
    fig, ax = plt.subplots(1, figsize=(10, 6))
    ax.axis('off')
    # print(crime)
    # if len(crime)==0:
    #     crime = ['Murder']
    ax.set_title(f'State Wise {crime[0]} Crime Data', fontdict={'fontsize': '25', 'fontweight' : '3'})
    plt.rcParams['savefig.facecolor']='#6FEDD6'
    p.plot(column=crime[0], cmap='viridis', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    plt.savefig('Application\static\images\mew_plot.png',bbox_inches='tight',pad_inches=0.5)
    options = ['Murder','Theft','Rape','Kidnap','Total']
    selected = crime[0]
    # tweets = tweet()
    # desc = ctype
    # crimetype = ctype
    # location = tweets[2]
    return render_template("home.html",name = 'new_plot', url ='static\images\mew_plot.png',options = options,selected=selected)
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")
    
@app.route("/predict", methods=['GET','POST'])
def predict():
    options = ['Murder','Theft','Rape','Kidnap','Total']
    selected = options[0]
    text = request.form['texttw']
    ctype,loc = predict_tweet(text)
    return render_template("home.html",name = 'new_plot', url ='static\images\mew_plot.png',options = options,selected=selected,desc=text,crimetype=ctype,location=loc)

if __name__ == "__main__":
    app.run(debug=True)