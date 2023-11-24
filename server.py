import socket
import time
import threading
from tkinter import *
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Assuming you have the necessary data and model trained before running this script
dataframe = pd.read_csv("spam.csv", encoding="latin-1")
dataframe.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'],
               inplace=True, axis=1)
dataframe['v1'].replace({'ham': '1', 'spam': '0'}, inplace=True)
dataframe.drop_duplicates(inplace=True)

cv = CountVectorizer()
x = dataframe['v2']
y = dataframe['v1']
x = cv.fit_transform(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = MultinomialNB()
model.fit(x_train, y_train)

cv = CountVectorizer()


def recv(clientsocket):
    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage == "":
            # sendermessages = [sendermessage]
            # checkmsg = cv.transform(sendermessages)
            # prediction = model.predict(checkmsg)
            # print(prediction)
            time.sleep(5)
            print("Client : " + sendermessage)


def start_server():
    listensocket = socket.socket()
    port = 3050
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('127.0.0.1', port))
    listensocket.listen(maxconnection)

    while True:
        (clientsocket, address) = listensocket.accept()
        t = threading.Thread(target=recv, args=(clientsocket,))
        t.start()


if __name__ == "__main__":
    start_server()
