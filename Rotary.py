import Encoder
from RPi import GPIO


GPIO.setmode(GPIO.BCM)


clk = 17
dt = 18
sw = 27


enc = Encoder.Encoder(dt, clk)

def swClicked(channel):
        if GPIO.input(sw) == 0:
            print ("Clicked ")
            sleep(0.3)
            
def main():
    
    print("Counter ", enc.read())
            
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
GPIO.add_event_detect(sw, GPIO.FALLING, callback=swClicked, bouncetime=1)
