#!/usr/bin/python
import socket 
import threading
from pyfiglet import Figlet
import datetime

f = Figlet(font='slant')
text = "Bennin App"
newText = f.renderText(text)
print(f"\033[1;31m{newText}\033[0m")
print("\t \t \033[1;32m********************************\033[0m") 
print("\t \t \033[1;32m   Coded by Crazy and Bennin\033[0m")
print("\t \t \033[1;32m**********************************\033[0m")  
print("")
 


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 5000))
sock.listen(1)

print("\033[1;33m[*] server on, waiting for connection....\033[0m")

conn,address = sock.accept()
print(f"\033[33m [-] Connected by {address}")

def receive_messages():
    
    while True:
        try:
            message = conn.recv(4096).decode()
            if not message:
                print("\033[1;31m[!] Client disconnected\033[0m")
                break
            print(f"\n\033[1:35m [-]{message} \033[0m")
        except:
            break
threading.Thread(target=receive_messages, daemon=True).start()

name = input("\033[1;35m [?] Enter your name: \033[0m").capitalize()

while True:
    try:
        time = datetime.datetime.now().strftime("%H:%M")
        text = input("\033[1;37m [+] You: \033[0m")
        full_message = (f"[{time}] {name} : {text}")
        conn.send(full_message.encode())
        fullMessage = (f"[[+] You{time}] {text}")
    except:
        print("\033[1;31m[!] Error sending message\033[0m")
        break

conn.close()
sock.close()