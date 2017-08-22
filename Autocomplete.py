import requests
import json
import pprint
from Google_API_PyQuest import api_request

API_Key = api_request()

def again():
	while True:
			print("Would you like to search again?")
			print("Press [Y] to search again")
			print("Press [N] to quit")
			
			again = input(": ").upper()
			
			if again not in ('Y','N'):
				print("Please choose [Y]es or [N]o")
				continue
			elif again in ('Y', 'N'):
				if again == "Y":
					search()
				elif again == "N":
					print("Thank you for using Google Autocomplete by Fletcher!")
					exit()
					
		

def search():
	while True:
		try:
			city = str(input("What city would you like to search for?: "))
			break
		except TypeError:
			print("Oops! Enter a valid input!")
		

	url = "https://maps.googleapis.com/maps/api/place/autocomplete"
	data_type = "/json"
	input_type = "?input=" + city
	# search_type = "types=(cities)" # This can specify whether we're looking at a city, zip, or general search

	API_URL = url + data_type + input_type + "&"  + "&key=" + API_Key # + search_type

	r = requests.get(API_URL)

	r_json = r.json()

	try:
		print("\n")
		print("\t" + r_json['predictions'][0]['description'])
		print("\n")
	except IndexError:
		print("\n")
		print("I'm sorry, that search doesn't match any records!")
		print("\n")

	
	again()
	

	

print("""
---------------------------------------------------------------------------
		Welcome to Google Autocomplete API by Charles Fletcher!
---------------------------------------------------------------------------
""")

search()