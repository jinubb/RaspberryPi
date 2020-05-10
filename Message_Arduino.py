import serial

arduino = serial.Serial('/dev/ttyACM0', 9600)

c = '5'

c=c.encode('utf-8')

arduino.write(c)
