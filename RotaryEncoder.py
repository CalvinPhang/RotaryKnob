import Encoder
from RPi import GPIO
from time import sleep

class RotaryEncoder:
    def __init__(self, clk, dt, sw, cw_function=0, ccw_function=0, clkdwn_function=0, clkup_function=0):
        self.clk = clk
        self.dt = dt
        self.sw = sw
        self.enc = Encoder.Encoder(dt, clk)
        if cw_function != 0:
            self.cw_function = cw_function
        else:
            self.cw_function = self.null_func
        if ccw_function != 0:
            self.ccw_function = ccw_function
        else:
            self.ccw_function = self.null_func
        if clkdwn_function != 0:
            self.clkdwn_function = clkdwn_function
        else:
            self.clkdwn_function = self.null_func
        if clkup_function != 0:
            self.clkup_function = clkup_function
        else:
            self.clkup_function = self.null_func
        
    def null_func(self):
        pass
    
    def sw_clicked(self, channel):
        if GPIO.input(self.sw) == 0:
            self.clkdwn_function()
            print ("CLICKED")
            while GPIO.input(self.sw) == 0:
                pass
            self.clkup_function()
    
    def run(self):
        
        GPIO.setup(self.sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.sw, GPIO.FALLING, callback=self.sw_clicked, bouncetime=1)      
        pos = self.enc.read()
        
        while True:
            read = self.enc.read()//2
            if read > pos:
                self.cw_function()
                print("CLOCKWISE")
            elif read < pos:
                self.ccw_function()
                print("COUNTER CLOCKWISE")
            pos = read
            


