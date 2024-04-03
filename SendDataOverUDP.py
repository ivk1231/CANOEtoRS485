import socket
import time


def send_command(payload, destination_ip, destination_port, source_port):
    try:
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.bind(("192.168.0.8", source_port))
                sock.connect((destination_ip, destination_port))
                sock.sendall(bytes.fromhex(payload))
                print(f"Command {payload} sent successfully.")
                time.sleep(0.5)
                # Uncomment the following lines if expecting a response
                # data, addr = sock.recvfrom(1024)
                # print(f"Received Modbus command response from {addr}: {data.hex()}")
    except OSError as e:
        print(f"Error: {e.strerror}. Check network settings or permissions.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    PAYLOAD = "01 03 00 00 00 01 84 0A"
    DESTINATION_IP = "192.168.0.7"
    DESTINATION_PORT = 5678
    SOURCE_PORT = 1234

    send_command(PAYLOAD, DESTINATION_IP, DESTINATION_PORT, SOURCE_PORT)
