from preprocess import Custom_Preprocessor
from location_extractor import get_locations

import numpy as np
import pickle
from tensorflow import keras

labels = {0:'Crime', 1:'Non-Crime'}
category_labels = {0: 'Kidnap', 1: 'Murder', 2: 'Rape', 3: 'Theft'}
model_path = './Weights/LSTM/26.73_89.10'
category_path = './Weights/LSTM Category/36.96_87.49'

Preprocessor = Custom_Preprocessor()

text = '@DailyMonitor Omg! They need to sue this bus company and driver for vehicular murder!!!!'

def predict_tweet(text):
    preprocessed_text =  Preprocessor.preprocess_data_x(text,single_entry=True)[0]
    locations = get_locations(preprocessed_text, get_state_of_cities=True, single_entry=True)[0]

    crime_model = keras.models.load_model(model_path+'/model')
    with open(model_path+'/tokenizer.pickle', 'rb') as handle:
        crime_tokenizer = pickle.load(handle)
    crime_padded = Preprocessor.tokenise(crime_tokenizer, [preprocessed_text], maxlen=len(preprocessed_text.split()))
    crime_prediction = crime_model.predict(crime_padded)

    if np.argmax(crime_prediction)==1:
        return None

    category_model = keras.models.load_model(category_path+'/model')
    with open(category_path+'/tokenizer.pickle', 'rb') as handle:
        category_tokenizer = pickle.load(handle)
    category_padded = Preprocessor.tokenise(category_tokenizer, [preprocessed_text], maxlen=len(preprocessed_text.split()))
    new_prediction = category_model.predict(category_padded)
    return category_labels[np.argmax(new_prediction)], locations

print(predict_tweet(text))