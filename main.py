#!/usr/bin/env python3
"""
Python to arduino serial sample
"""
import serial
import time

__author__ = "Hackspace"
__license__ = "MIT"
# sirib0400

def main():
    # start serial connection, change first argument based on microcontroller's serial port
    ser = serial.Serial('/dev/cu.usbserial-14130', 9600, timeout=1)
    # Sleep for 1 second to wait for connection to establish
    time.sleep(1)
    while True:
        # send 1 to arduino
        ser.write(b'1')
        # sleep 1 second to wait for reply
        time.sleep(1)
        # sleep 1 second to wait for reply
        if ser.in_waiting:
            line = ser.readline()
            print(line.decode('unicode_escape'))

    ser.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
