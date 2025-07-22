💬 Python Echo Server – Simple Chat with Commands
Welcome to the Python Echo Server Project!
This project lets people connect to a server, chat by sending text messages, and get replies. It's great for learning socket programming, multi-client chat, and user authentication in Python.

📌 What Does It Do?
✅ Users can log in with a username and password
✅ They can send messages and get replies from the server
✅ Server supports multiple users at the same time
✅ Users can send special commands to get help, see who is online, or view their chat history
✅ All chats are saved with timestamps in a log file
✅ Each user has a personal history file
✅ Messages can be sent to everyone connected

📁 Project Files
server.py->	The main server code that handles login, chat, and commands
client.py	->The client code to connect and chat with the server
users.txt	->A file that stores allowed usernames and passwords
logs/	Folder-> where all chat logs are saved with date and time
history/	->Folder where each user's personal chat history is stored

🔐 Sample Usernames & Passwords:
Create a file named users.txt in the project folder like this:
alice:pass123
bob:qwerty
admin:admin123
Each line has a username and password separated by a :
👉 Users must log in with one of these.

💻 How to Run the Project:
✅ Step 1: Start the Server
Open a terminal or command prompt and run:
bash:
python server.py
You’ll see:
[+] Server started on port 1024
✅ Step 2: Run the Client
Open another terminal (or another device) and run:
bash:
python client.py
The client will ask for:
Username
Password
Once logged in, you can chat!

💡 What Can You Type?:
You Type	              What Happens
Hello	You             get: You said: Hello
/help	                See list of commands
/users	              See who is online
/history	            See your personal message history
/quit	                 Disconnect from server

📝 Example Chat:
You: Hi there
Server: You said: Hi there
You: /users
Server: Active users: alice, bob
You: /history
Server: (shows your past messages)
You: /quit
Server: Disconnected from server.

