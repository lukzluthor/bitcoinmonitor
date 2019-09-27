#!/usr/bin/env python
from dot3k import backlight
backlight.rgb(0,255,0)
#backlight.rgb(255,255,255)

import fcntl
import socket
import struct

import dothat.lcd as lcd

import coinbase
from coinbase.wallet.client import Client

api_key = 'yourapikey'
api_secret = 'yourapisecret'



import datetime
datetime.datetime.now()

dataz=(datetime.datetime.now())

from time import gmtime, strftime
gezell = strftime("%a, %d %b %Y %X +0000", gmtime())


from coinbase.wallet.client import Client
client = Client(api_key, api_secret)
client.get_exchange_rates()


currency_code = 'USD'  # can also use EUR, CAD, etc.

# Make the request
price = client.get_spot_price(currency=currency_code)

print 'Current bitcoin price in %s: %s' % (currency_code, price.amount)

xprice = price.amount

def get_addr(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return 'Not Found!'

wlan0 = get_addr('wlan0')
host = socket.gethostname()
lcd.clear()

lcd.set_cursor_position(0,0)
#lcd.write('{}'.format(host))
lcd.write('{}'.format(dataz))
#lcd.write('{}'.format(gezell))

lcd.set_cursor_position(0,1)
lcd.write('BTC ${}'.format(xprice))

lcd.set_cursor_position(0,2)
if wlan0 != 'Not Found!':
    lcd.write(wlan0)
else:
    lcd.write('wlan0 {}'.format(wlan0))
