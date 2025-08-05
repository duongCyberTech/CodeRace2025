# 🔌Code Race Challenge 2025 Project

A simple Python socket-based project demonstrating how to process CAN signals into physical data.

## 📁 Project Structure

```
├── .gitignore
├── Code_Race
    ├── can-docker
    │   └── Dockerfile
    ├── dbc_processing
    │   ├── dbc_v2.py
    │   └── error_detection.py
    ├── decode_signals.py
    ├── output_binary.png
    ├── p_data
    │   ├── description.csv
    │   ├── error_signals_summary.csv
    │   ├── msg.txt
    │   ├── signals_summary.csv
    │   └── signals_summary_v2.csv
    ├── raw_data
    │   └── BOSCH_CAN Data.dbc
    ├── receive_testing.py
    ├── receive_v2.py
    ├── requirements.txt
    └── send_v2.py
└── README.md
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
