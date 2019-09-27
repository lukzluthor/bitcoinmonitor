# bitcoinmonitor
monitor the bitcoin price on a DisplayOTron LCD and a PI Zero

file tab contains your entry for cron.
this will be added to the root user's cron tab

the file bitcoin.py you need to move into /etc/
make sure you edit bitcoin.py and add your coinbase API key and secret.

#install displayOtron python drivers
curl https://get.pimoroni.com/displayotron | bash

#install the dot3k drivers
sudo pip install dot3k

#install your coinbase api client
pip install coinbase

#you will need to login to your coinbase wallet and generate an API key
#you will enter the key and secret in the bitcoin.py file.
#move the file into /etc/
mv bitcoin.py /etc/

I have the pi zero with LCD wired up on my night stand to check the bitcoin price.

-- LukzLuthor   

https://keybase.io/cgfx

If you found this helpful send me some lumens on keybase.
cgfx*keybase.io


