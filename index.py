import requests
 
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

f = open("weblist_metaboosting.csv", "r")
# f = ["https://www.sveltetraining.net" ,
# "https://metaboosting.com" , 
# "https://www.tamaslim.com",
# "https://get.riseworkouts.com",
# "https://go.riseworkouts.com",
# "https://www.oneanddoneworkouts.com", 
# "https://get.metaboosting.com", 
# "https://www.metaboosting.com"]

for x in f:
    CHECKGTM(x)


