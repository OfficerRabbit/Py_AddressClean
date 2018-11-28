# Project

This is an API project I'm working on that utilizes the Google Autocomplete API to take part of an address, city through zipcode, and returns the top choice.

## Notes

The Google_API_PyQuest module is ignored in this as it contains my personal Google API Key code. The api_request() module simply returns a Google API Key; you can remove the PyQuest import and have API_Key = [Your Google API Key]

## Files

1. Autocomplete.py
	* Prompt the user for a city and then look up the city with Google Autocomplete, returning data found or asking to try again
2. Google_API_PyQuest.py
	* GoogleAPI key module, used in Py_Address_Test.py and Py_Address_Clean.py to pull API key
3. 