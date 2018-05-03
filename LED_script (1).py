import RPi.GPIO as GPIO #importing GPIO contorls
import time #importing time
import datetime #importing datetime that allows for print real time

#multiprocessing or MULTITHREADING: runnning several functions in parallel
from multiprocessing import Process

GPIO.setmode(GPIO.BOARD) #using board pin numbering
GPIO.setup(7, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #maybe include the pud down optionprint GPIO.input(4)


#callbacks i.e. what to do if GPIO is rising
GPIO.add_event_detect(16, GPIO.RISING) #detect if the input on GPOI4 is rising or falling
def my_callback():
    print "BOLD TR acquired!",
    print datetime.datetime.now()

Blink(int(iterations),float(speed1), float(speed2))
GPIO.add_event_callback(16, my_callback) #add callback

def Blink(numTimes,speed1, speed2):
    for i in range(0,numTimes):
        print "Iteration " + str(i+1)
        GPIO.output(7,True)
        time.sleep(speed1)
        GPIO.output(7,False)
        time.sleep(speed2)
        

iterations = 300 #raw_input("Enter total nr of times to blink: ")
speed1 = 0.01 #raw_input("Enter length of each blink in s: ")
speed2 = 0.09 #emprirically this results in apprx 10 blinks per second, ie 10Hz

#Block Design
def Blink_total():
    print "short waiting period of 20s"
    time.sleep(20)
    print "Block 1",
    print datetime.datetime.now()
    
    Blink(int(iterations),float(speed1), float(speed2))
    time.sleep(60)
    print "Block 2",
    print datetime.datetime.now()
    Blink(int(iterations),float(speed1), float(speed2))
    time.sleep(60)
    print "Block 3",
    print datetime.datetime.now()
    Blink(int(iterations),float(speed1), float(speed2))
    time.sleep(60)
    print "Block 4",
    print datetime.datetime.now()
    Blink(int(iterations),float(speed1), float(speed2))
    time.sleep(60)
    

Blink_total()
#running my_callback and Blink_total in parallel
#https://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel
if __name__ == '__main__':
  p1 = Process(target=my_callback)
  p1.start()
  p2 = Process(target=Blink_total)
  p2.start()
  p1.join()
  p2.join()

#finish
GPIO.cleanup()
