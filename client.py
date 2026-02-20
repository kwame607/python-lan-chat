#!/usr/bin/python
import socket
import threading
import datetime
from pyfiglet import Figlet

f = Figlet(font='slant')
text = "Bennin App"
newText = f.renderText(text)
print(f"\033[1;31m{newText}\033[0m")
print("\t \t \033[1;32m********************************\033[0m") 
print("\t \t \033[1;32m   Coded by Crazy and Bennin\033[0m")
print("\t \t \033[1;32m**********************************\033[0m")  
print("")



host = "127.0.0.1"
port = 5000

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

print("\033[1:33m [!] Connected to Crazy \033[0m")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(4096).decode()
            if not message:
                print("\033[1;31m[!] Server disconnected\033[0m")
                break
            print(f"\n\033[1:35m [-]{message} \033[0m")
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

name = input("\033[1;35m [?] Enter your name: \033[0m").capitalize()
print("\n")

while True:
    try:
        time = datetime.datetime.now().strftime("%H:%M")
        text = input("\033[1;37m [+] You: \033[0m")
        full_message = (f"[{time}] {name} : {text}")
        client_socket.send(full_message.encode())
        fullMessage = (f"[[+] You{time}] {text}")
    except:
        print("\033[1;31m[!] Error sending message\033[0m")
        break


client_socket.close()