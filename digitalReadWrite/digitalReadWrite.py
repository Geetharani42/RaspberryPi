#libraries importing
import RPi.GPIO as gpio

#pin declarations
inp = 21
outp = 20

#setting no warnings
gpio.setwarnings(False)

#setting bcm mode
gpio.setmode(gpio.BCM)

#pin direction setting
gpio.setup(inp, gpio.IN)
gpio.setup(outp, gpio.OUT)

#main loop
while True:
            #data reading digitally
            k = gpio.input(inp)
     
           #condition
           if k == 1:
                 gpio.output(outp, 1)    #setting output as high
           else:           #if the threshold condition fails
                gpio.output(outp, 0)    #setting output as low
          