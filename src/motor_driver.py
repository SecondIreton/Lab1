class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin (There will be several pin parameters)
        """
        # If enpin is high motor/vice versa
        en_pin.low ()
        # Setup Timer
        tim = pyb.Timer(timer, freq=20000) 
        # Setup Channel
        ch1 = tim.channel(1, pyb.Timer.PWM, pin=in1pin)
        ch2 = tim.channel(2, pyb.Timer.PWM, pin=in2pin)
        print ("Creating a motor driver")

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        print (f"Setting duty cycle to {level}")
        
        
        
if __name__ == '__main__'
# Section for testing code?
'''
moe = MotorDriver (a_pin, another_pin, a_timer)
moe.set_duty_cycle (-42)
'''
