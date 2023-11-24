import socket
import time
import threading
from tkinter import *

root = Tk()
root.geometry("300x500")
root.config(bg="white")
sa = 0




def start_server():
    # global model
    listensocket = socket.socket()
    port = 3023
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('127.0.0.1', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()
    # port=port+1

    while True:
        (clientsocket, address) = listensocket.accept()
        print("Accepted connection from", address)
        client_thread = threading.Thread(
            target=handle_client, args=(clientsocket,))
        client_thread.start()


def handle_client(clientsocket):
    print(clientsocket)
    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage:
            break  # If the client closes the connection, exit the loop
        print(sendermessage)
        lstbx.insert(0, "Client : " + sendermessage)


def func():
    t = threading.Thread(target=start_server)
    t.start()


startchatimage = PhotoImage(file='start.png')

buttons = Button(root, image=startchatimage, command=func, borderwidth=0)
buttons.place(x=90, y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message, font=(
    'calibre', 10, 'normal'), border=2, width=32)
messagebox.place(x=10, y=550)

sendmessageimg = PhotoImage(file='send.png')

sendmessagebutton = Button(root, image=sendmessageimg,
                           command=start_server, borderwidth=0)
sendmessagebutton.place(x=260, y=440)

lstbx = Listbox(root, height=20, width=43)
lstbx.place(x=15, y=80)

user_name = Label(root, text=" Number", width=10)

root.mainloop()
