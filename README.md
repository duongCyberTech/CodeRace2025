# 🔌Code Race Challenge 2025 Project

A simple Python socket-based project demonstrating how to process CAN signals into physical data.

## 📁 Project Structure

```
.
├── send_v2.py         # Socket server
├── receive_v2.py         # Socket client
├── requirements.txt  # Required packages (if any)
└── README.md         # This file
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/duongCyberTech/CodeRace2025.git
cd CodeRace2025/CodeRace
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate.bat     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python send_v2.py
```

### 5. Run the Client (in a new terminal)

```bash
python receive_v2.py
```

---

## 🛠 Features

- TCP socket communication
- Server accepts multiple clients
- Client can send and receive messages

---
