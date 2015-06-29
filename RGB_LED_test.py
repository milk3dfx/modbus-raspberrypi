import RPi.GPIO as GPIO
import time

pins = {'r' : 18, 'g': 23, 'b' : 24}

if __name__ == "__main__":
	state = 0
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	
	GPIO.setup(pins['r'], GPIO.OUT)
	GPIO.setup(pins['g'], GPIO.OUT)
	GPIO.setup(pins['b'], GPIO.OUT)
	
	try:
		while True:
			r = state%2;
			g = (state>>1)%2
			b = (state>>2)%2
			print r, g, b
			
			if state is 8:
				state = 0
			else:
				state += 1
			time.sleep(0.5)
	except KeyboardInterrupt:
		print "Exiting"
	except Exception:
		traceback.print_exc(file=sys.stdout)
		
	GPIO.cleanup()
	print "Done"
	sys.exit(0)