import time, datetime.datetime
import requests
import RPi.GPIO as GPIO
import telepot
import urllib2
import sys
import Adafruit_DHT
from telepot.loop import MessageLoop

white = 26 #light
yellow = 19 #fan
red = 13 #ac
green = 6 #door
GPIO.setmode(GPIO.BCM)
#LED White
GPIO.setup(white, GPIO.OUT)
GPIO.output(white, 0) #Off initially
#LED Yellow
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, 0) #Off initially
#LED Red
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, 0) #Off initially
#LED green
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, 0) #Off initially

GPIO.setup(3,GPIO.OUT) #GPIO 3 -> Green LED as output
GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,0)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,0)


def vicky(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    upt = datetime.datetime.now()
    print 'Received: %s' % command

    if command == 'Hi':
        telegram_bot.sendMessage (chat_id, str("Hi! Vicky"))

    if command == 'Light on':
	   GPIO.output(white, 1)
	   telegram_bot.sendMessage (chat_id, str("Living Room Light Up"))

    elif command == 'Light off':
	    GPIO.output(white, 0)
    	dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
    	telegram_bot.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "Light", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
    	requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field1=%s' % (tm))


    if command == 'Fan on':
        GPIO.output(yellow, 1)
    	telegram_bot.sendMessage (chat_id, str("Living Room Fan Up"))

    elif command == 'Fan off':
        GPIO.output(yellow, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot.sendMessage (chat_id, str("Living Room Fan Off"))
        payload = { "Name" : "Vicky", "Object": "Fan", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field2=%s' % (tm))

    if command == 'Ac on':
    	GPIO.output(red, 1)
    	telegram_bot.sendMessage (chat_id, str("Living Room Air Conditioner Up"))

    elif command == 'Ac off':
    	GPIO.output(red, 0)
    	dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "AC", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field3=%s' % (tm))


    if command == 'Door lock':
    	GPIO.output(5, 1)
    	telegram_bot.sendMessage (chat_id, str("Door Locked"))
        time.sleep(3) 
        GPIO.output(5, 0)

    elif command == 'Door unlock':
    	GPIO.output(green, 1)
    	telegram_bot.sendMessage (chat_id, str("Door Unlocked By Vicky"))
    	telegram_bot1.sendMessage (chat_id, str("Door Unlocked By Vicky"))
        telegram_bot2.sendMessage(chat_id , str("Door Unlocked By Vicky"))

    if command == 'Help':
    	telegram_bot.sendMessage (chat_id, str("Sorry Help less"))

    if command == 'Logdata':
    	r = requests.post("http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/retrieve")
    	telegram_bot.sendMessage (chat_id, str(r.json()))
    

def duck(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    upt = datetime.datetime.now()
    print 'Received: %s' % command

    if command == 'Hi':
        telegram_bot1.sendMessage (chat_id, str("Hi! Keerthana"))

    if command == 'Light on':
       GPIO.output(white, 1)
       telegram_bot1.sendMessage (chat_id, str("Living Room Light Up"))

    elif command == 'Light off':
        GPIO.output(white, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot1.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "Light", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field1=%s' % (tm))


    if command == 'Fan on':
        GPIO.output(yellow, 1)
        telegram_bot1.sendMessage (chat_id, str("Living Room Fan Up"))

    elif command == 'Fan off':
        GPIO.output(yellow, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot1.sendMessage (chat_id, str("Living Room Fan Off"))
        payload = { "Name" : "Vicky", "Object": "Fan", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field2=%s' % (tm))

    if command == 'Ac on':
        GPIO.output(red, 1)
        telegram_bot1.sendMessage (chat_id, str("Living Room Air Conditioner Up"))

    elif command == 'Ac off':
        GPIO.output(red, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot1.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "AC", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field3=%s' % (tm))


    if command == 'Door lock':
        GPIO.output(5, 1)
        telegram_bot1.sendMessage (chat_id, str("Door Locked"))
        time.sleep(3) 
        GPIO.output(5, 0)

    elif command == 'Door unlock':
        GPIO.output(green, 1)
        telegram_bot.sendMessage (chat_id, str("Door Unlocked By Keerthana"))
        #telegram_bot1.sendMessage (chat_id, str("Door Unlocked By Vicky"))
        telegram_bot2.sendMessage(chat_id , str("Door Unlocked By Keerthana"))

    if command == 'Help':
        telegram_bot1.sendMessage (chat_id, str("Sorry Help less"))

    if command == 'Logdata':
        r = requests.post("http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/retrieve")
        telegram_bot1.sendMessage (chat_id, str(r.json()))

def barath(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    upt = datetime.datetime.now()
    print 'Received: %s' % command

    if command == 'Hi':
        telegram_bot2.sendMessage (chat_id, str("Hi! Vicky"))

    if command == 'Light on':
       GPIO.output(white, 1)
       telegram_bot2.sendMessage (chat_id, str("Living Room Light Up"))

    elif command == 'Light off':
        GPIO.output(white, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot2.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "Light", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field1=%s' % (tm))


    if command == 'Fan on':
        GPIO.output(yellow, 1)
        telegram_bot2.sendMessage (chat_id, str("Living Room Fan Up"))

    elif command == 'Fan off':
        GPIO.output(yellow, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot2.sendMessage (chat_id, str("Living Room Fan Off"))
        payload = { "Name" : "Vicky", "Object": "Fan", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field2=%s' % (tm))

    if command == 'Ac on':
        GPIO.output(red, 1)
        telegram_bot2.sendMessage (chat_id, str("Living Room Air Conditioner Up"))

    elif command == 'Ac off':
        GPIO.output(red, 0)
        dt = datetime.datetime.now()
        diff = divmod((datetime.datetime.now()-upt).total_seconds(), 60)
        tm=int(diff[0])
        telegram_bot2.sendMessage (chat_id, str("Living Room Light Down"))
        payload = { "Name" : "Vicky", "Object": "AC", "Time_in": tm.__str__() }
        headers = {'content-type': 'application/json'}
        requests.post('http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/postdata', data=json.dumps(payload), headers=headers)
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field3=%s' % (tm))


    if command == 'Door lock':
        GPIO.output(5, 1)
        telegram_bot2.sendMessage (chat_id, str("Door Locked"))
        time.sleep(3) 
        GPIO.output(5, 0)

    elif command == 'Door unlock':
        GPIO.output(green, 1)
        telegram_bot.sendMessage (chat_id, str("Door Unlocked By Barath"))
        telegram_bot1.sendMessage (chat_id, str("Door Unlocked By Barath"))
        #telegram_bot2.sendMessage(chat_id , str("Door Unlocked By Vicky"))

    if command == 'Help':
        telegram_bot.sendMessage (chat_id, str("Sorry Help less"))

    if command == 'Logdata':
        r = requests.post("http://ec2-18-232-64-191.compute-1.amazonaws.com:3000/retrieve")
        telegram_bot.sendMessage (chat_id, str(r.json()))
    

	
#Ravian2bot
telegram_bot = telepot.Bot('970046755:AAE1Y1Dw090GmCJuobqZt1Nf_Oob7dGBRV4')
#Keerthanabot
telegram_bot1 = telepot.Bot('810449538:AAHgkUDvcqX9YSn-78oK66t6sjTYfR-yxIY')

#Barath Bot
telegram_bot2 = telepot.Bot('807505290:AAHHeLFytNlt6Te0eektIB3qXrDQtNVptzI')


print(telegram_bot.getMe())
print(telegram_bot1.getMe())
print(telegram_bot2.getMe())	

MessageLoop(telegram_bot, vicky).run_as_thread()
MessageLoop(telegram_bot1, duck).run_as_thread()
MessageLoop(telegram_bot2, barath).run_as_thread()
print("Launch Control")



while 1:
    if(GPIO.input(14)==False): #object is near
         GPIO.output(3,True) #Green
    else:
        GPIO.output(3,False)

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    
    if(int(temperature)> 20):
        GPIO.output(17,0)

    urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field4=%s' % (temperature))
    urllib2.urlopen('https://api.thingspeak.com/update?api_key=7BDCW06SENBIO6KT&field5=%s' % (humidity))

