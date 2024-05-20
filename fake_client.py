# just to test the fake_zapper.py server capabilities


import zmq
import time

def setup_socket_req(port):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")
    return socket

if __name__ == "__main__":
    socket = setup_socket_req(5556)
    while True:

        socket.send(b"beep")

        msg = socket.recv()
        print(f"received {msg}")
        time.sleep(5)