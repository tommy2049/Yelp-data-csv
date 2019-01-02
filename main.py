import json 
from yelpapi import YelpAPI

api_key = ""
yelp_api = YelpAPI(api_key)
search_results = yelp_api.search_query(term="vape",location="montreal", sort_by="rating",limit=50)

data = json.dumps(search_results)
data = json.loads(data)

def getAddress(address_array):
	address = ""
	for i in range(len(address_array)):
		address = address + address_array[i] + " "
	address = address.replace(",", "")
	return address

f = open("data.csv", "w+")
f.write("Name,,Number,Address" + "\n")
f.close()

f = open("data.csv", "a+")
for i in range(len(data["businesses"])):
	address = getAddress(data["businesses"][i]["location"]["display_address"])
	f.write(data["businesses"][i]["name"] + ",," + data["businesses"][i]["phone"] + "," + address + "\n")
f.close()

