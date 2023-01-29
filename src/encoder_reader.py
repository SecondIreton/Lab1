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

