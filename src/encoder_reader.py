"""!
@file encoder_reader.py
This file contains code which computes the reading from the encoder in order to evaluate the speed of the motor

@author Mech12
@date   30-Jan-2023
"""

import pyb # Micropython library

class EncoderReader:
    """!
    Compute the value of the encoder reading
    @returns The encoder reading
    """
    timer = None

    def __init__(self, pinA, pinB, timerNum):
        """!
        Sets the channels and timer for the motor that is running
        """
        self.timer = pyb.Timer (timerNum, freq=20000)
        ch1 = self.timer.channel(1, pyb.Timer.ENC_A, pin=pinA)
        ch2 = self.timer.channel(2, pyb.Timer.ENC_B, pin=pinB)

    def read(self):
        """!
        @returns The encoder reading
        """
        return self.timer.counter()

    def zero(self):
        """!
        Sets the time counter to 0
        """
        self.timer.counter(0)

if __name__ == "__main__":
    # Section for testing code
    pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)
    test = EncoderReader(pinB6, pinB7, 4)
    test.zero()
    while True:
        print(test.read())