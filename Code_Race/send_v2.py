import socket
import threading
import time
import random

HOST = '127.0.0.1'
PORT = 5000
arb_ids = [0x1a6, 0x374, 0x295, 0x13c]

def generate_fake_can_frame():
    arb_id = random.choice(arb_ids)
    dlc = random.randint(1, 8)
    data = [random.randint(0, 255) for _ in range(dlc)]
    return arb_id, data

def handle_client(conn):
    try:
        while True:
            arb_id, data = generate_fake_can_frame()
            high = (arb_id >> 8) & 0xFF
            low = arb_id & 0xFF
            dlc = len(data)
            frame = [high, low, dlc] + data
            message = ' '.join(f'{b:02X}' for b in frame) + '\n'
            conn.sendall(message.encode())
            print(f"Sent: {message.strip()}")
            time.sleep(1)
    except BrokenPipeError:
        print("Client disconnected.")
    finally:
        conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] TCP CAN Server listening on {HOST}:{PORT}")
conn, addr = server.accept()
print(f"[+] Client connected from {addr}")
handle_client(conn)
