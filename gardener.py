# gardener.py
LIGHT_PIN = 20
PUMP_PIN = 12

import threading
import schedule
import time
import atexit

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(PUMP_PIN, GPIO.OUT)

class GardenerAction(object):
	turnOn = "on"
	turnOff = "off"

def threaded(job_func, action=GardenerAction.turnOn, forLength=None):
    job_thread = threading.Thread(target=job_func, kwargs={'action': action, 'forLength': forLength})
    job_thread.start()

def water(action=GardenerAction.turnOn, forLength=None):
	toggleComponent(PUMP_PIN, action, forLength)

def light(action=GardenerAction.turnOn, forLength=None):
	toggleComponent(LIGHT_PIN, action, forLength)

def toggleComponent(pin, action=GardenerAction.turnOn, forLength=None):
	if (forLength is not None):
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(forLength)
		GPIO.output(pin, GPIO.LOW)
	else:
		if action == GardenerAction.turnOn: GPIO.output(pin, GPIO.HIGH)
		else: GPIO.output(pin, GPIO.LOW)

def exit_handler():
    GPIO.cleanup()

atexit.register(exit_handler)



# Turn water on every 30 minutes for 10 seconds
schedule.every(30).minutes.do(threaded, water, forLength=10)

# Other scheduling examples
#schedule.every().hour.do(threaded, light, forLength=300)
#schedule.every().day.at("10:30").do(threaded, light, action=GardenerAction.turnOn)
#schedule.every().day.at("12:30").do(threaded, light, action=GardenerAction.turnOff)
#schedule.every().monday.do(threaded, water, forLength=30)
#schedule.every().wednesday.at("13:15").do(threaded, light, forLength=30)




while True:
    schedule.run_pending()
    time.sleep(1)
