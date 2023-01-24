import re
import torch

from torch.optim import Adam
from tqdm import tqdm
from BertModel import Dataset

class Custom_Trainer:
    def __init__(self, epochs, batch_size, labels, LABEL_COLUMN, learning_rate=0.001, decay=0):
        self.epochs = epochs
        self.batch_size = batch_size
        self.lr = learning_rate
        self.decay = decay
        self.labels = labels
        self.label_column = LABEL_COLUMN

    def preprocess_data_x(self, data, get_word_count = False, single_entry=False):
        text_list = []
        word_count = []

        if single_entry:
            data = [data]
        
        for entry in data:
            new_text = re.sub("[^a-zA-Z ]", " ", entry)
            new_text = [word for word in new_text.lower().split() if word not in self.STOPWORDS]
            word_count.append(len(new_text))
            new_text = ' '.join(new_text)
            text_list.append(new_text)    
            
        if get_word_count:
            return text_list, word_count
        else:
            return text_list

    def train(self, model, train_data, val_data, tokenizer, early_stop = False) -> None:
        train = Dataset(train_data, tokenizer, self.labels, self.label_column)
        val = Dataset(val_data, tokenizer, self.labels, self.label_column)

        train_dataloader = torch.utils.data.DataLoader(train, batch_size=self.batch_size, shuffle=True)
        val_dataloader = torch.utils.data.DataLoader(val, batch_size=self.batch_size)

        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda:0" if use_cuda else "cpu")

        criterion = torch.nn.CrossEntropyLoss()
        optimizer = Adam(model.parameters(), lr=self.lr, weight_decay=self.decay)

        if use_cuda:
                model = model.cuda()
                criterion = criterion.cuda()

        for epoch_num in range(self.epochs):
                total_acc_train = 0
                total_loss_train = 0
                total_acc_val = 0
                total_loss_val = 0

                for train_input, train_label in tqdm(train_dataloader):
                    train_label = train_label.to(device)
                    mask = train_input['attention_mask'].to(device)
                    input_id = train_input['input_ids'].squeeze(1).to(device)

                    output = model(input_id, mask)
                    
                    batch_loss = criterion(output, train_label.long())
                    total_loss_train += batch_loss.item()
                    
                    acc = (output.argmax(dim=1) == train_label).sum().item()
                    total_acc_train += acc

                    model.zero_grad()
                    batch_loss.backward()
                    optimizer.step()

                with torch.no_grad():
                    for val_input, val_label in val_dataloader:
                        val_label = val_label.to(device)
                        mask = val_input['attention_mask'].to(device)
                        input_id = val_input['input_ids'].squeeze(1).to(device)

                        output = model(input_id, mask)

                        batch_loss = criterion(output, val_label.long())
                        total_loss_val += batch_loss.item()
                        
                        acc = (output.argmax(dim=1) == val_label).sum().item()
                        total_acc_val += acc
            
                print(f"Epochs: {epoch_num + 1} "\
                        "| Train Loss: {total_loss_train / len(train_data): .3f} "\
                        "| Train Accuracy: {total_acc_train / len(train_data): .3f} "\
                        "| Val Loss: {total_loss_val / len(val_data): .3f} "\
                        "| Val Accuracy: {total_acc_val / len(val_data): .3f}")

    def evaluate(self, model, test_data, tokenizer) -> float:
    
        test = Dataset(test_data, tokenizer, self.labels, self.label_column)

        test_dataloader = torch.utils.data.DataLoader(test, batch_size=self.batch_size)

        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda" if use_cuda else "cpu")

        if use_cuda:

            model = model.cuda()

        total_acc_test = 0
        with torch.no_grad():

            for test_input, test_label in test_dataloader:

                test_label = test_label.to(device)
                mask = test_input['attention_mask'].to(device)
                input_id = test_input['input_ids'].squeeze(1).to(device)

                output = model(input_id, mask)

                acc = (output.argmax(dim=1) == test_label).sum().item()
                total_acc_test += acc
        test_accuracy = total_acc_test / len(test_data)
        print(f'Test Accuracy: {test_accuracy: .3f}')

        return test_accuracy