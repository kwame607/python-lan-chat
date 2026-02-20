# python-lan-chat
Python-based LAN chat application using sockets and threading

## Overview
A local area network (LAN) chat application built with Python, enabling real-time messaging between multiple clients on the same network. This project demonstrates **socket programming, threading, and client-server communication**.

## Features
- Real-time text messaging over LAN  
- Supports multiple clients connecting to a single server  
- Simple and user-friendly command-line interface  
- Threaded design for handling multiple connections concurrently  

## Technologies Used
- Python 3  
- Socket programming  
- Threading  

## Project Structure
```

python-lan-chat/
│
├── main_server.py   # Server application
├── client.py        # Client application
├── README.md
└── requirements.txt # Optional if you used external libraries

````

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-lan-chat.git
cd python-lan-chat
````

2. Run the server first:

```bash
python main_server.py
```

3. Run one or more clients:

```bash
python client.py
```

4. Enter the server IP (if required) and start chatting over your LAN.

---

## Usage

* Each client can send messages to all connected clients in real-time.
* Works only within the local network (LAN).
* Ideal for learning network programming and basic client-server architecture.

---

## Future Enhancements

* Optional GUI using Tkinter or PyQt
* Message encryption for secure communication
* File transfer capability

---

## Author

Kwame Emmanuel Adom (CRAZY)
Networking & Python Developer

