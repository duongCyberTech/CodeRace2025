import socket
from receive_testing import parse_raw_can_frame
from decode_signals import gen_signal

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("[+] Connected to TCP CAN Server")

try:
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        for line in data.strip().split('\n'):
            print(f"Received CAN frame: {line}")
            raw_input = [int(byte, 16) for byte in line.split()]
            parsed = parse_raw_can_frame(raw_input)
            print(raw_input)
            print("**")
            print(f"Arbitration ID: 0x{parsed['arbitration_id']:X}")
            print(f"DLC: {parsed['dlc']}")
            print(f"Data: {parsed['data']}")
            print("____________")
            gen_signal(parsed)
            print("=============================================")

except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    client.close()
