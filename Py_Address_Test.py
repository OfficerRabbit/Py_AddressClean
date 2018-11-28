# Import, pay yer tariffs!
import pypyodbc
import requests
import json
from pprint import pprint
from Google_API_PyQuest import api_request

# Global Variables
url = "https://maps.googleapis.com/maps/api/place/autocomplete"
data_type = "/json"
input_type = "?input="
API_Key = api_request()

clean_test = {"name": 'Charles Clean',
              "address": '4085 Tudor Centre Drive',
              "city": 'Anchorage',
              "state": 'AK',
              "zip": '99508',
              }

mess_test = {"name": 'Charles Messy',
             "address": '4085 Tudr Centr Dr',
             "city": 'Achnorage',
             "state": 'Akaska',
             "zip": '99508',
             }


to_test = mess_test

test_name = to_test['name']
test_address = to_test['address']
test_city = to_test['city']
test_state = to_test['state']
test_zip = to_test['zip']
test_full = to_test['address']+' '+to_test['city']+' '+to_test['state']+' '+to_test['zip']


print("< Name: {0}>\n".format(test_name))
print("< Address: {0}>\n".format(test_address))
print("< City: {0}>\n".format(test_city))
print("< State: {0}>\n".format(test_state))
print("< ZIP: {0}>\n".format(test_zip))
print("< Full Address: {0}>\n".format(test_full))


state_url = url + data_type + input_type + test_zip + "&types=(regions)"+ "&key=" + API_Key

print("< API URL: {0}>".format(state_url))

r = requests.get(state_url, verify = False)

r_json = r.json()

pprint(r_json, indent = 2)

'''
zip_url = url + data_type + input_type + test_zip + "&types=(regions)"+ "&key=" + API_Key

print("< API URL: {0}>".format(zip_url))

r = requests.get(zip_url, verify = False)

r_json = r.json()

pprint(r_json, indent = 2)



full_url = url + data_type + input_type + test_full + "&"  + "&key=" + API_Key

print("< API URL: {0}>".format(full_url))

r = requests.get(full_url, verify = False)

r_json = r.json()

pprint(r_json, indent = 2)
'''
