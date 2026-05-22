# web_chat_app
Real-time web chat application built for instant messaging.
# Web Chat App

A real-time chat application built using Django and Django Channels.

Users can:

* Create and join chat rooms
* Send real-time messages
* Login and logout securely
* Communicate instantly using WebSockets

---

# Features

* User Authentication
* Real-Time Messaging
* Chat Rooms
* WebSocket Communication
* Django Channels Integration
* Responsive Chat UI
* Message Storage in Database
* Online Chat System

---

# Technologies Used

* Python
* Django
* Django Channels
* HTML
* CSS
* JavaScript
* SQLite3
* Bootstrap
* WebSockets

---

# Project Structure

```bash
web_chat_app/
│
├── chat_app/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── registration/
│   │   └── login.html
│   ├── base.html
│   ├── room.html
│   └── rooms.html
│
├── web_chat_app/
│   ├── asgi.py
│   ├── consumers.py
│   ├── routing.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
