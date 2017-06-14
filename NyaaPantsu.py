#!/usr/bin/python
import sys, getopt
import requests
from pprint import pprint

def main(argv):
	# Config NEEDED or have to be called by python
	url = "https://nyaa.pantsu.cat/api/upload"
	username = "myusername"
	apiToken = "myapitoken"
	torrentToUpload = ""
	category = "3_12"
	language = "en-us"

	# Optional Config
	description = "Uploaded by NyaaPantsu remote"
	remake = "false"
	hidden = "false"
	name = ""
	magnet = ""
	website = ""

	helptext = "NyaaPantsu.py -u <username> -a <apitoken> -i <torrentfile> -m <magnetlink> -n <torrentname> -c <category> -l <language> -d <description -r <apiurl> -w <website> --remake --hidden"
	try:
		opts, args = getopt.getopt(argv,"hi:u:r:a:m:n:c:l:d:w:",["ifile=","username=","apiurl=","apitoken=","magnet=","name=","cat=","lang=","desc=", "website=","remake","hidden"])
	except getopt.GetoptError:
		print(helptext)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(helptext)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			torrentToUpload = arg
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-r", "--apiurl"):
			url = arg
		elif opt in ("-a", "--apitoken"):
			apiToken = arg
		elif opt in ("-m", "--magnet"):
			magnet = arg
		elif opt in ("-n", "--name"):
			name = arg
		elif opt in ("-c", "--cat"):
			category = arg
		elif opt in ("-l", "--lang"):
			language = arg
		elif opt in ("-d", "--desc"):
			description = arg
		elif opt in ("-w", "--website"):
			website = arg
		elif opt in ("--remake"):
			remake = "true"
		elif opt in ("--hidden"):
			hidden = "true"
	data = {
		'language':language,
		'c':category,
		'magnet':magnet,
		'username':username,
		'name':name,
		'desc':description,
		'website_link':website,
		'remake':remake,
		'hidden':hidden
	}
	if torrentToUpload != "":
		response = requests.post(url,
			data=data,
			files={'torrent': open(torrentToUpload, 'rb')},
			headers={ 'Authorization': apiToken })
	else:
		response = requests.post(url,
			data=data,
			headers={ 'Authorization': apiToken })
	pprint(response.json())

if __name__ == "__main__":
   main(sys.argv[1:])