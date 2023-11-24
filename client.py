import socket


def sendmsg():
    s = socket.socket()
    hostname = '127.0.0.1'  # Replace with the IP address or hostname of the server
    port = 3023

    s.connect((hostname, port))
    msg = input("Enter your message: ")
    if msg=="end" :
        s.close()
    s.send(msg.encode())


if __name__ == "__main__":
    while True:
        sendmsg()
