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
    """ Main entry point of the app """
    ser = serial.Serial('/dev/cu.usbserial-14130', 9600, timeout=1)
    time.sleep(1)
    while True:
        ser.write(b'1')
        time.sleep(1)
        line = ser.readline()
        print(line.decode('unicode_escape'))

        '''
        ser.write(b'0')
        time.sleep(1)
        line = ser.readline()
        print(line.decode('unicode_escape'))
        '''
    ser.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()