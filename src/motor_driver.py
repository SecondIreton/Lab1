import pyb

class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """
    
    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin Represents the pin for enabling and 
               disabling the motor
        @param in1pin Is 1 of 2 pins used for controlling the 
               magnitude and direction of the motor
        @param in2pin Is 1 of 2 pins used for controlling the 
               magnitude and direction of the motor
        @param timer Is a variable representing the Timer used
               for the motor
        """
        # If enpin is high motor/vice versa
        en_pin.low()
        # Setup Timer
        tim = pyb.Timer(timer, freq=20000) 
        # Setup Channel
        ch1 = tim.channel(1, pyb.Timer.PWM, pin=in1pin)
        ch2 = tim.channel(2, pyb.Timer.PWM, pin=in2pin)
        return(ch1,ch2,tim)
        print ("Creating a motor driver")

    def set_duty_cycle (self, level, ch1, ch2):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        @param ch1 A variable representing timer channel 1 
               to be called for PWM command
        @param ch2 A variable representing timer channel 2 
               to be called for PWM command
        """
        if level >= 0:
            ch1.pulse_width_percent(level)
            ch2.pulse_width_percent(0)
        else:
            level = level/(-1)
            ch2.pulse_width_percent(level)
            ch1.pulse_width_percent(0)
        
        print (f"Setting duty cycle to {level}")
        
        
        
#if __name__ == __main__:
    # Section for testing code?
    '''
    moe = MotorDriver (a_pin, another_pin, a_timer)
    moe.set_duty_cycle (-42)
    '''
