import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def CHECKGTM(url):
    print('checking : '+url)
    r = requests.get(url)
    htmlBody = str(r.content)
    if htmlBody.find('GTM-NH8V9ZX') != -1:
        print("GTM FOUND")
        print("*********************************\n")
    else:
        print("GTM not found")
        print("*********************************\n")

def purifyString(st):
    st = st.replace('%0a', '')
    return st

def getdata(url):
	r = requests.get(url)
	return r.text
dict_href_links = {}
def get_links(website_link):
	html_data = getdata(website_link)
	soup = BeautifulSoup(html_data, "html.parser")
	list_links = []
	for link in soup.find_all("a", href=True):

		# Append to list if new link contains original link
		if str(link["href"]).startswith((str(website_link))):
			list_links.append(link["href"])

		# Include all href that do not start with website link but with "/"
		if str(link["href"]).startswith("/"):
			if link["href"] not in dict_href_links:
				print(link["href"])
				dict_href_links[link["href"]] = None
				link_with_www = website_link + link["href"][1:]
				print(link_with_www)
				list_links.append(link_with_www)

	# Convert list of links to dictionary and define keys as the links and the values as "Not-checked"
	dict_links = dict.fromkeys(list_links)
	return dict_links

f = open("weblists.txt", "r")
# f = ["https://www.sveltetraining.net" ,
# "https://metaboosting.com" , 
# "https://www.tamaslim.com",
# "https://get.riseworkouts.com",
# "https://go.riseworkouts.com",
# "https://www.oneanddoneworkouts.com", 
# "https://get.metaboosting.com", 
# "https://www.metaboosting.com"]
print(get_links("https://metaboosting.com"))
# for x in f:
#     print (purifyString(x))
#     CHECKGTM(purifyString(x))

