#importing libraries
import RPi.GPIO as GPIO

#Pin declaration for keypad rows and columns
L1 = 18
L2 = 23
L3 = 24
L4 = 25

C1 = 10
C2 = 9
C3 = 11
#C4 = 21  #uncomment this when 4x4 keypad is used

#Setting no warnings mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  #BCM mode setting

#Pin direction setting
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #uncomment #this when 4x4 keypad is used

#readline function defining
 def readLine(line, characters):
                #making all lines high one by one
                GPIO.output(line, GPIO.HIGH)
                #checking for which column output is high
                if(GPIO.input(C1) == 1):
                    #printing according character
                    print(characters[0])
                if(GPIO.input(C2) == 1):
                    print(characters[1])
                if(GPIO.input(C3) == 1):
                    print(characters[2])   
                #if(GPIO.input(C4) == 1): #uncomment these two #lines when using 4x4 keyoad
                    #print(characters[3]) 
                #making all lines low again            
                GPIO.output(line, GPIO.LOW)

while True:
    readLine(L1, ["1","2","3"])
    readLine(L2, ["4","5","6"])
    readLine(L3, ["7","8","9"])
    readLine(L4, ["*","0","#"])
