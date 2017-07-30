# gardener.py
import threading
import schedule
import time
import atexit

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)

LIGHT_PIN = 18
PUMP_PIN = 20

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





schedule.every(30).seconds.do(threaded, water, forLength=5)
#schedule.every(30).seconds.do(threaded, light, action=GardenerAction.turnOff)

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)





while True:
    schedule.run_pending()
    time.sleep(1)