import RPi.GPIO as GPIO
import time
import argparse
import sys, traceback

from pymodbus.client.sync import ModbusTcpClient

led_pin = 21
pin_status = 1
update_interval = 0.1

if __name__ == "__main__":
	
	print "=== Modbus client (Single LED) ==="
	parser = argparse.ArgumentParser(description='Modbus client')
	parser.add_argument('ip',  default='localhost', help='IP adress of modbus server')
	args = parser.parse_args()
	
	client = ModbusTcpClient(args.ip)

	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(led, GPIO.OUT)
	
	try:
		while True:
			result = client.read_coils(1, 1)
			status = result.bits[0]
			print status
			GPIO.output(led, pin_status)
			time.sleep(update_interval)
	except KeyboardInterrupt:
		print "Stopping program"
	except Exception:
		traceback.print_exc(file=sys.stdout)	
	GPIO.cleanup()
	client.close()
	print "Done"
	sys.exit(0)
