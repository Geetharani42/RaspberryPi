#importing libraries
from pyfingerprint.pyfingerprint import PyFingerprint
import serial
import RPi.GPIO as gpio
import time

#Pin declarations for switches
enrol=5
delet=6
inc=13
dec=19
iden=26

#Setting no warnings
gpio.setwarnings(False)

#setting bcm mode
gpio.setmode(gpio.BCM)

#selecting pin directions with software pullup
gpio.setup(enrol, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(delet, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(inc, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(dec, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(iden, gpio.IN, pull_up_down=gpio.PUD_UP)

#checking for fingerprint sensor through hardware serial pins 
#with 9600 as baud rate
try:
    f = PyFingerprint('/dev/ttyS0', 9600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('Exception message: ' + str(e))
    exit(1)

#when enroll switch pressed
def enrollFinger():
    print('Waiting for finger...')
    #if image of finger not read from sensor simply pass(No #operation)
    while ( f.readImage() == False ):
        pass
    #when finger placed
    f.convertImage(0x01)
    #search for template whether it is already stored #fingerprint or not
    result = f.searchTemplate()
    #Storing the position Number of detected fingerprint
    positionNumber = result[0]
    #if found result shows value greater than or equal to 0
    if ( positionNumber >= 0 ):
        #if greater than -1 means finger already stored &
#enrolling function will get exist
        print('Template already exists at position #' + str(positionNumber))
        return
#if not found in stored templates try to read another image
    print('Remove finger...')
    print('Waiting for same finger again...')
    while ( f.readImage() == False ):
        pass
    f.convertImage(0x02)
    #Compare the stored to sets of image
    if ( f.compareCharacteristics() == 0 ):
        #if not same means data won't get stored
        print("Fingers do not match")
        return
    #if same means create a new template and store data
    f.createTemplate()
    positionNumber = f.storeTemplate()
    print('Finger enrolled successfully!')
    print('New template position #' + str(positionNumber))
    time.sleep(2)
#when search switch is pressed
def searchFinger():
    print('Waiting for finger...')
    #If finger is not placed, no operation will happen
    while( f.readImage() == False ):
        time.sleep(.5)
        #return
    #when finger placed means search for the template
    f.convertImage(0x01)
    result = f.searchTemplate()
    #finding the template id of detected finger
    positionNumber = result[0]
    accuracyScore = result[1]
    #if found id is -1 then no finger like that is in data
    if positionNumber == -1 :
        print('No match found!')
        return
    #if found id is not -1, then print the template id of found 
#finger
    else:
        print('Found template at position #' + str(positionNumber))

#when delete switch is pressed
def deleteFinger():
    positionNumber = 0
    count=0
  # when enroll switch not pressed execute this loop only
    while gpio.input(enrol) == True:   
        #when inc switch is pressed, increase count value by 1
        if gpio.input(inc) == False:
            count=count+1
            if count>1000:
                count=1000
            time.sleep(0.2)
        #when dec switch is pressed, decrease count value by 1
        elif gpio.input(dec) == False:
            count=count-1
            if count<0:
                count=0
            time.sleep(0.2)
    #assign count to positionNumber
    positionNumber=count
    #delete fingerprint under that positionNumber
    if f.deleteTemplate(positionNumber) == True :
        print('Template deleted!')

#main loop
while True:
        #when enroll switch is pressed, call enroll function
        if gpio.input(enrol) == 0:
            enrollFinger()
        #when delete switch is pressed, call delete function
        elif gpio.input(delet) == 0:
            while gpio.input(delet) == 0:
                time.sleep(0.1)
                deleteFinger()
        #when search switch is pressed, call search function
        elif gpio.input(iden)==0:
            searchFinger()

