#!/usr/bin/env python

import RPi.GPIO as GPIO, time, os, numpy as np, urllib2, urllib
from scipy.interpolate import interp1d

DEBUG = 1
GPIO.setmode(GPIO.BCM)

#RCtime misst die Zeit, die gebraucht wird um einen Kondensator zu befüllen
#RCpin = 18 misst Temperatur, RCpin = 16 misst Helligkeit
def RCtime (RCpin):

	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)

	GPIO.setup(RCpin, GPIO.IN)

	while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
	return reading

#lux führt eine lineare Interpolation mit der gemessenen Zeit durch und gibt den dazugehörigen Luxwert zurück
def lux(bri):

	x = np.array([0,     1,     20,   45,   50,   70,  120, 165, 220, 300, 750, 2200, 3000, 3400, 1000000])
	y = np.array([17000, 13000, 3000, 1900, 1500, 500, 350, 165, 100, 80,  20,  5,    1,    0,    0])

	f = interp1d(x, y)

	bri = f(bri)
	return bri

#cel führt eine lineare Interpolation mit der gemessenen Zeit durch und gibt den dazugehörigen Celsiuswert zurück
def cel(tmp):

	x = np.array([11250, 12750, 15500, 17000, 18500, 20000, 30000])
	y = np.array([42,    34.8,  23.2,  10,    8.4,   0,    -23.2])

	f = interp1d(x, y)

	tmp = f(tmp)
	return tmp

#send führt einen POST-Befehl auf den im Netzwerk befindlichen Ruby on Rails Server aus und überträgt so die gemessenen Daten
def send(bri, tmp):
	
	values = {'lux':bri,
		'cel':tmp}
	values = urllib.urlencode(values)
	#IP im eduroam
	path = 'http://77.80.22.161:3000/get_values'
	values = values.encode('utf-8')
	req = urllib2.Request(path, values)
	req.add_header("Content-type", "application/x-www-form-urlencode")
	page = urllib2.urlopen(req).read()
	print page

#Endlosschleife die die oben angeführten Funktionen unendlich wiederholt
#Wird das Script gerade erst gestartet wird zehnmal RCtime ausgeführt ohne die gemessenen Daten weiter zu verarbeiten, da die ersten vier bis acht Messungen erfahrungsgemäß total daneben liegen
t = 0
while True:
	
	if(t < 10):
		RCtime(18)
		t = t+1
		print "Calibrating: "
		print t*10
		time.sleep(1)
	else:
		tmp = RCtime(18)
		tmp = cel(tmp)
		bri = RCtime(16)
		bri = lux(bri)
		send (bri, tmp)
		time.sleep(1)