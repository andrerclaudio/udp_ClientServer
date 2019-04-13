# external libraries
import socket
import time

# addressing information of target
IPADDR = '192.168.0.255'
PORTNUM_DEST = 54321
PORTNUM_SOURCE = 12345

# enter the data content of the UDP packet as hex
MESSAGE = "i am here"
PACKETDATA = bytes(MESSAGE, "utf-8")


def application():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.settimeout(0.2)
    s.bind(('', PORTNUM_SOURCE))

    while True:
        s.sendto(PACKETDATA, ('<broadcast>', PORTNUM_DEST))
        time.sleep(3)

    return True


def main():
    application()
    return None


if __name__ == "__main__":
    # Run the main function.
    main()
