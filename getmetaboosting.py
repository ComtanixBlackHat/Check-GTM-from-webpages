import requests
 
def CHECKGTM(url):
    # print('checking : '+url)
    r = requests.get(url)
    htmlBody = str(r.content)
    if htmlBody.find('GTM-NH8V9ZX') != -1:
        print(url+"|GTM FOUND")
       
    else:
        print(url+"|GTM Not Found")
       

f = ["https://get.metaboosting.com/" ,"https://get.metaboosting.com/articles/"
"https://get.metaboosting.com/contact/" , "https://get.metaboosting.com/careers/","https://get.metaboosting.com/sit-to-fit/" ,
"https://get.metaboosting.com/healthy-made-simple/", 
"https://get.metaboosting.com/cdn-cgi/l/email-protection" , 
"https://get.metaboosting.com/why-your-weight-wont-budge/"]

for x in f:
    CHECKGTM(x)
