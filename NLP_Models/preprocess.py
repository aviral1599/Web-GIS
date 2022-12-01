import re
import nltk
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Custom_Preprocessor:
    def __init__(self, trunc_type = 'post', pad_type = 'post') -> None:
        nltk.download('stopwords')

        from nltk.corpus import stopwords

        self.STOPWORDS = set(stopwords.words('english'))
        self.TRUNC_TYPE= trunc_type
        self.PADDING_TYPE = pad_type

    def set_max_seq_length(self, max_seq_length):
        self.MAX_SEQUENCE_LENGTH = max_seq_length

    def preprocess_data_x(self, data, get_word_count = False, single_entry=False):
        text_list = []
        word_count = []

        if not single_entry:
            for entry in data:
                new_text = re.sub("[^a-zA-Z ]", " ", entry)
                new_text = [word for word in new_text.lower().split() if word not in self.STOPWORDS]
                word_count.append(len(new_text))
                new_text = ' '.join(new_text)
                text_list.append(new_text)
        else:
            new_text = re.sub("[^a-zA-Z ]", " ", data)
            new_text = [word for word in new_text.lower().split() if word not in self.STOPWORDS]
            word_count.append(len(new_text))
            new_text = ' '.join(new_text)
            text_list.append(new_text)
        
        if get_word_count:
            return text_list, word_count
        else:
            return text_list

    def tokenise(self, tokenizer, data, maxlen=None, padding=None, truncating=None):
        if not maxlen:
            maxlen = self.MAX_SEQUENCE_LENGTH
        if not padding:
            padding = self.PADDING_TYPE
        if not truncating:
            truncating = self.TRUNC_TYPE
        
        data_sequences = tokenizer.texts_to_sequences(data)
        data_padded = pad_sequences(data_sequences, maxlen=maxlen, padding=padding, truncating=truncating)
        return data_padded