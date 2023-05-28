import requests
 
def CHECKGTM(url):
    # print('checking : '+url)
    r = requests.get(url)
    htmlBody = str(r.content)
    if htmlBody.find('GTM-NH8V9ZX') != -1:
        print(url+"|GTM FOUND")
        # print("*********************************\n")
    else:
        print("GTM not found")
        # print("*********************************\n")
s = [
"https://get.riseworkouts.com/articles/", 
"https://get.riseworkouts.com/" ,
"https://get.riseworkouts.com/sit-to-fit/", 
"https://get.riseworkouts.com/careers/" ,
"https://get.riseworkouts.com/contact/" ,
"https://get.riseworkouts.com/healthy-made-simple/",
"https://get.riseworkouts.com/why-your-weight-wont-budge/", 
"https://get.riseworkouts.com/cdn-cgi/l/email-protection"]

for x in s:
    CHECKGTM(x)