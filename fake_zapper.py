# This file is used to test how does communication between C# and python takes place
# We will use a socket port approach with zero mq
# The python part is gonna act as a server that waits for the client to start the stimulation
import numpy
import zmq
import sounddevice as sd



def beep():
    fs = 16000
    myrec = numpy.load('beep.npy')
    sd.play(myrec, fs)
    sd.wait()



def setupServer(port):
    context = zmq.Context()
    socket = context.socket(zmq.REP) # we specify the type of socket we want
    socket.bind(f"tcp://*:{port}")
    return socket

def setupSUB(port, topic = "FES"):
    cont = zmq.Context()
    socket = cont.socket(zmq.SUB)
    socket.connect(f"tcp://localhost:{port}")
    socket.subscribe("FES")
    #socket.setsockopt_string(zmq.SUBSCRIBE, topic)
    return socket


def check_message(message, topic):
    message = message.decode('utf-8')

    if message == topic:
        return 0
    elif 'True' in message:
        return True
    else:
        return False

if __name__ == "__main__":

    topic = 'FES'
    socket = setupSUB(5556) # lets try a different format
    i = 0
    while True:
        message = socket.recv() # Here im waiting for the type od stimulation FES device should deliver
        message = check_message(message, topic)
        print(f'{i}: {message}')
        if message:
            beep()
        i = i+1