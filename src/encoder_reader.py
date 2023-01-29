import pyb


class EncoderReader:
    timer = None

    def __init__(self, pinA, pinB, timerNum):
        self.timer = pyb.Timer (timerNum, freq=20000)
        ch1 = self.timer.channel(1, pyb.Timer.ENC_A, pin=pinA)
        ch2 = self.timer.channel(2, pyb.Timer.ENC_B, pin=pinB)

    def read(self):
        return self.timer.counter()

    def zero(self):
        self.timer.counter(0)

if __name__ == "__main__":
    # Section for testing code?
    pinB6 = pyb.Pin (pyb.Pin.board.PB6, pyb.Pin.IN)
    pinB7 = pyb.Pin (pyb.Pin.board.PB7, pyb.Pin.IN)
    test = EncoderReader(pinB6, pinB7, 4)
    test.zero()
    while True:
        print(test.read())