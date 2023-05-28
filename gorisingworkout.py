import requests
 
def CHECKGTM(url):
    # print('checking : '+url)
    r = requests.get(url)
    htmlBody = str(r.content)
    if htmlBody.find('GTM-NH8V9ZX') != -1:
        print(url+"|GTM FOUND")
        # print("*********************************\n")
    else:
        print(url+"|GTM not found")
        # print("*********************************\n")
s = ["https://go.riseworkouts.com/articles/", 
"https://go.riseworkouts.com/",
"https://go.riseworkouts.com/sit-to-fit/" ,"https://go.riseworkouts.com/careers/" 
"https://go.riseworkouts.com/contact/",
"https://go.riseworkouts.com/healthy-made-simple/",
"https://go.riseworkouts.com/why-your-weight-wont-budge/", 
"https://go.riseworkouts.com/cdn-cgi/l/email-protection"]

for x in s:
    CHECKGTM(x)
