# external libraries
import socket

# addressing information of target
PORTNUM_DEST = 54321
PORTNUM_SOURCE = 12345

# enter the data content of the UDP packet as hex
MESSAGE = "i am here"
PACKETDATA = bytes(MESSAGE, "utf-8")


def application():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(('', PORTNUM_DEST))

    while True:
        data, addr = client.recvfrom(1024)

        if data == PACKETDATA:
            print("received message: %s" % data)

    return True


def main():
    application()
    return None


if __name__ == "__main__":
    # Run the main function.
    main()