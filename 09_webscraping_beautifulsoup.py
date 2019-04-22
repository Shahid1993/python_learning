# Import the libraries needed
import requests
import time
from bs4 import BeautifulSoup


print ("----------------------------------")

# The URL to scrape
url = 'https://www.popsugar.com/celebrity/Kit-Harington-Rose-Leslie-Cutest-Pictures-42389549'
#url = 'https://www.bing.com/images/search?q=jon+snow&FORM=HDRSC2'


# Connecting
response = requests.get(url)

# Grab the HTML and using Beautiful
soup = BeautifulSoup(response.text, 'html.parser')

#A loop code to run through each link, and download it
for i in range(len(soup.findAll('img'))):
	tag = soup.findAll('img')[i]
	link = tag['src']

	#skip it if it doesn't start with http
	if "http" in link:
		print("Grabbed url : "+link)

		filename = str(i) + '.jpg'
		print("Download : "+filename)
		try:
			r = requests.get(link)
			open(filename, 'wb').write(r.content)
		except Exception as e:
			print("Not able to download : "+link);
		
	else:
		print("Grabbed url (skip) : "+ link)

	time.sleep(1) #Breaking down the code

