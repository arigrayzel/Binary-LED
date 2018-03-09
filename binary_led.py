import RPi.GPIO as GPIO
import time

#set up GPIO using board numbering
GPIO.setmode(GPIO.BCM)
light1 = 4
light2 = 12
light3 = 16
GPIO.setup(light1, GPIO.OUT, initial = 0)
GPIO.setup(light2, GPIO.OUT, initial = 0)
GPIO.setup(light3, GPIO.OUT, initial = 0)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#false means the button is pressed
button = True
previous = True
n = 0 
i1 =0
i2 =0
i3 =0
while (True):

    button = GPIO.input(18)
    
    if button == False and previous == True:
        n = n+1
        

        if True:
            if i1 ==0:
                i1 = 1
            elif i1 ==1:
                i1 = 0

        if n%2 ==0:
            if i2 == 1:
                i2 = 0
            else:
                i2 = 1
        if n%4 ==0:
            if i3 ==1:
                i3 = 0
            else:
                i3 = 1


    previous = button
 
    print n


    i3s = str(i3)
    i2s = str(i2)
    i1s = str(i1)
    print i3s + i2s + i1s
    if i3 ==1:
        GPIO.output(light3, GPIO.HIGH)
    else:
        GPIO.output(light3, GPIO.LOW)
    if i2 ==1:
        GPIO.output(light2, GPIO.HIGH)
    else:
        GPIO.output(light2, GPIO.LOW)
    if i1 ==1:
        GPIO.output(light1, GPIO.HIGH)
    else:
        GPIO.output(light1, GPIO.LOW)
    time.sleep(.1)

GPIO.cleanup()
""" nprint = n #nprint used to count the binary without modifying n
    
    if nprint > 3:
        i3 = 1
        nprint = nprint -4
    else:
        i3 = 0

    if nprint > 1:
        i2 = 1
        nrprint = nprint - 2
    else:
        i2 = 0

    if nprint >0:
        i1 =1
    else:
        i1 = 0"""
