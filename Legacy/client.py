import socket
import sys
import time

HOST, PORT = "192.168.0.101", 9999
#data = "x".join(sys.argv[1:])
data = 0

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.send(bytes(str(data) + "\n","utf8"))

    # Receive data from the server and shut down
    received = sock.recv(1024)
    #sock.close()

    print("Sent:     %s" % data)
    print("Received: %s" % received)

    #sock.shutdown(SHUT_RDWR)
    sock.close()

    data += 1
    time.sleep(2)
