
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

# f = open("weblist_metaboosting.csv", "r")
f =["https://www.metaboosting.com",
"http://metaboosting.com/",
"https://get.metaboosting.com/order/us/mbc/?skin=mbc&usfid=mbcflow01",
"https://get.metaboosting.com/order/us/mbc/?skin=mbc&usfid=mbcflow01&product_name=64",
"https://metaboosting.com/",
"https://metaboosting.com/sit-to-fit/?tid=102037d37d719201ac87cdeda53468&aff_id=1499&offer_id=58&bo=mbps&aff_sub=&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=10205dbe8ee0ea8f3e37ca527f314c&aff_id=1499&offer_id=58&bo=mbps&aff_sub=&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102067bbd79ce8148cdbbb95eced98&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN",
"https://metaboosting.com/sit-to-fit/?tid=102087b797d3de5b180238363ea405&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1020b9a0f5c918cd553d069066a064&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN",
"https://metaboosting.com/sit-to-fit/?tid=1020c205722dd80aef1882b495a9b2&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metSignal&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1020cb95a56b3694d54105ccc87bb9&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=10219fa0db4d64db970f4eb70f44d8&aff_id=1499&offer_id=58&bo=mbps&aff_sub=",
"https://metaboosting.com/sit-to-fit/?tid=1021bc997d00b1b108892dfbd2d63e&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metWaqas&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1021d9f0a18a96046b6bd6b54fb04d&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1022cf7b6ca3bd996bdc28072b2477&aff_id=1249&offer_id=58&bo=mbps&aff_sub=pomonanyc&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102303a2726aa595fb508b34717a99&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN",
"https://metaboosting.com/sit-to-fit/?tid=1023698fd3e1fc9e2e60123cd9fff3&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob",
"https://metaboosting.com/sit-to-fit/?tid=10237de3f22480934c57a9ee97f96e&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102514d5cbdb306d0f1c3c8d85b709&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=10257416ab21a1b9d5acd5cec64ef6&aff_id=1499&offer_id=58&bo=mbps&aff_sub=&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=1025904eb7c0ae05823bf8f256c529&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob",
"https://metaboosting.com/sit-to-fit/?tid=10259bd8a006b6c18e86a1f0995645&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metSignal&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=10259ed6f1ee165d016d3f95e487e7&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1025fd20678d13a02c24843bc6d0e5&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty",
"https://metaboosting.com/sit-to-fit/?tid=10263c062b339e2bffc18eb83b565b&aff_id=1499&offer_id=58&bo=mbps&aff_sub=",
"https://metaboosting.com/sit-to-fit/?tid=102649f1af23057de877d6ef9356f8&aff_id=1253&offer_id=58&bo=mbps&aff_sub=SFEmet&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1026e8ea91edda2d93ae3bf02d67c7&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=10270ab0173bf6553811cb7333891e&aff_id=1499&offer_id=58&bo=mbps&aff_sub=&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=10270dd0a5b0c001f36a32c7cab33d&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102798575498a2914ef7196f8a9ad0&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metSignal&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1027d30be7314b69c3e4d8945c4ece&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metglobe",
"https://metaboosting.com/sit-to-fit/?tid=1028b4fabc7f55b5ba0ccdabd9f547&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102937789f25d735023fc96f43f2e2&aff_id=1249&offer_id=58&bo=mbps&aff_sub=pomonanyc&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102979bec5158081473065a221ca64&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=1029cb282f1d7002fd3b74a3014227&aff_id=1249&offer_id=58&bo=mbps&aff_sub=RMOLTC&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=1029da9c6fd2c22e1d7c6d68db48db&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob",
"https://metaboosting.com/sit-to-fit/?tid=102a22d6c9f693d650f7883e3bbd8c&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty",
"https://metaboosting.com/sit-to-fit/?tid=102a5659b6a4210b58811c4b94eb5a&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN",
"https://metaboosting.com/sit-to-fit/?tid=102a692a3eb34ed557656831b78fc6&aff_id=1499&offer_id=58&bo=mbps&aff_sub=",
"https://metaboosting.com/sit-to-fit/?tid=102b5bcf5d4f1758eb60c386ee7f76&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102b806b2cf506d21083771469fe26&aff_id=1249&offer_id=58&bo=mbps&aff_sub=pomonanyc&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102c834ede4d791bd87a66804536c9&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty",
"https://metaboosting.com/sit-to-fit/?tid=102cc0f24177a763ce25fd25c373cf&aff_id=1249&offer_id=58&bo=mbps&aff_sub=pomonanyc&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102d29fc1da2ae1e25dfb07f4bc6a6&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102d78cacc5561118591b9775e8335&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN",
"https://metaboosting.com/sit-to-fit/?tid=102d899d0242c95342a5fb63d77e0f&aff_id=1249&offer_id=58&bo=mbps&aff_sub=pomonanyc&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102e272ae43fa55bf9eb7e8fbf577d&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102e3e7f6f8128f78e276a5dee372d&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102e41155acad06b325b364b872b2f&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102e8f146885491d535870d7db5cbc&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102ee8bfdc49ed8a7fc58d258d3e72&aff_id=1499&offer_id=58&bo=mbps&aff_sub=",
"https://metaboosting.com/sit-to-fit/?tid=102f35f33cc479642e217ff9673384&aff_id=1249&offer_id=58&bo=mbps&aff_sub=RMOLTC&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102f83206e38d68288625a1bc496f5&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102f9cf23057728e8f31964f18610d&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metzob&aff_sub3=&aff_sub4=",
"https://metaboosting.com/sit-to-fit/?tid=102fdc9a49e82ae6004748156b0ec4&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metAPN&aff_sub3=",
"https://metaboosting.com/sit-to-fit/?tid=102fec96ad5a28b9647e1942c6cc85&aff_id=1253&offer_id=58&bo=mbps&aff_sub=metkaty&aff_sub3=&aff_sub4=",
"https://www.metaboosting.com/",
"https://www.metaboosting.com/boosted/",
"https://www.metaboosting.com/boosted/?tid=1027ce02f10e6355a9357bdba4ce0d&aff_id=2&offer_id=58&bo=mbps",
"https://www.metaboosting.com/boosted/?ut=n&aff_sub5=64539c80f1dff72e723ccc99",
"https://www.metaboosting.com/boosted/?ut=n&tid=brand_res&ADID=510568462956",
"https://www.metaboosting.com/contact/",
"https://www.metaboosting.com/lp/13-fat-melting-elixirs/?p=Mjk=&tid=1029635d5b7fbca411a1f2393b2b98&aff_id=1440&offer_id=59&bo=mbps&aff_sub5=&aff_sub3=",


"https://www.metaboosting.com/lp/superfood-desserts/",


"https://www.metaboosting.com/sit-to-fit-tb/transcript/",
"https://www.metaboosting.com/sit-to-fit/",
"https://www.metaboosting.com/sit-to-fit/005/",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=3",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=5555&ADID=550066815076",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=br3559",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=br5928",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=br8037&ADID=527031137426",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&ad=br8037&ADID=533813486846",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&aff_sub5=642aa3b601b611200c4c32f1",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&aff_sub5=general",
"https://www.metaboosting.com/sit-to-fit/005/?link=direct&offer_id=52&h=v2&tid=7662v11pc&ADID=552745274385",
"https://www.metaboosting.com/sit-to-fit/005/?tdc_uid=1169782",
"https://www.metaboosting.com/sit-to-fit/005/?tid=102067d39f4ff078df0385f3ddaa45&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=10221fadd30a6e2188f98c10c4b81f&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3=&aff_sub4=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=1025a6309c6204898f2bacf1448252&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=10275b6ba13ba95804ddd743149fdf&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3=&aff_sub4=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=1028f6414075ba1e1d2ef1780e4925&aff_id=1440&offer_id=58&bo=mbps&page=005&h=&aff_sub3=&aff_sub4=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=1028f6414075ba1e1d2ef1780e4925&aff_id=1528&offer_id=58&bo=mbps&page=005&h=&aff_sub3=&aff_sub4=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=102a018b0e18392ba1f1dd960939d7&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3=",
"https://www.metaboosting.com/sit-to-fit/005/?tid=102b16bb6a61c957a40780f7d81af2&aff_id=1065&offer_id=58&bo=mbps&page=005&h=&aff_sub3="
"https://www.metaboosting.com/sit-to-fit/005/?tid=102fd81d8edd2270b8eb27962b4324&aff_id=1065&offer_id=58&bo=mbps&page=005&h=",
"https://www.metaboosting.com/sit-to-fit/406283685/",
"https://www.metaboosting.com/special/",
"https://www.metaboosting.com/special/002/?bo=mbps&tid=102782d1502ed246e3c0f4af2f9c88&aff_id=1437&offer_id=59"]





s = [
"https://www.metaboosting.com/",
"https://www.metaboosting.com/contact/",
"https://www.metaboosting.com/articles/",
"https://www.metaboosting.com/sit-to-fit/",
"https://www.metaboosting.com/careers/",
"https://www.metaboosting.com",
"https://www.metaboosting.com/cdn-cgi/l/email-protection",
"https://www.metaboosting.com/healthy-made-simple/",
"https://www.metaboosting.com/why-your-weight-wont-budge/"]



for x in f:
    CHECKGTM(x)



