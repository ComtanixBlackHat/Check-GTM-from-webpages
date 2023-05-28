import requests
 
def CHECKGTM(url):
    # print(url+'|')
    r = requests.get(url)
    htmlBody = str(r.content)
    if htmlBody.find('GTM-NH8V9ZX') != -1:
        print(url+"|GTM Found")
        # print("*********************************\n")
    else:
        print(url+"|GTM Not Found")
        # print("*********************************\n")

# x = [
# "https://sveltetraining.com/",

# "https://sveltetraining.com/products",

# "https://sveltetraining.com/products",

# "https://sveltetraining.com/resources",

# "https://sveltetraining.com/resources",

# "https://sveltetraining.com/cart",

# "https://sveltetraining.com/about",

# "https://sveltetraining.com/about"	,

# "https://sveltetraining.com/contact",

# "https://sveltetraining.com/contact",

# "https://sveltetraining.com/video",

# "https://sveltetraining.com/video"	,

# "https://sveltetraining.com/terms",

# "https://sveltetraining.com/terms",

# "https://sveltetraining.com/privacy-policy",

# "https://sveltetraining.com/privacy-policy"	,

# "https://sveltetraining.com/testimonial-agreement"	,

# "https://sveltetraining.com/testimonial-agreement"	,

# "https://sveltetraining.com/ccpa"	,

# "https://sveltetraining.com/ccpa"	,	

# "https://sveltetraining.com/megagreens"	,

# "https://sveltetraining.com/megagreens"	,	

# "https://sveltetraining.com/blog-articles/7-easy-amp-effective-tips-to-fighting-sugar-cravings"	,

# "https://sveltetraining.com/blog-articles/7-easy-amp-effective-tips-to-fighting-sugar-cravings"	,	

# "https://sveltetraining.com/blog-articles/5-easy-healthy-habits-you-didnt-think-of"	,

# "https://sveltetraining.com/blog-articles/5-easy-healthy-habits-you-didnt-think-of"	,

# "https://sveltetraining.com/blog-articles/self-care-for-the-mind-amp-body"	,

# "https://sveltetraining.com/blog-articles/self-care-for-the-mind-amp-body"	,	

# "https://sveltetraining.com/blog-articles/the-ultimate-guide-to-going-out-amp-staying-on-track"	,

# "https://sveltetraining.com/blog-articles/the-ultimate-guide-to-going-out-amp-staying-on-track"	,	

# "https://sveltetraining.com/blog-articles/the-importance-of-posture-more-than-just-looks"	,

# "https://sveltetraining.com/blog-articles/the-importance-of-posture-more-than-just-looks"	,	

# "https://sveltetraining.com/blog-articles/better-sleep-for-a-better-life-5-tips-amp-tricks"	,

# "https://sveltetraining.com/blog-articles/better-sleep-for-a-better-life-5-tips-amp-tricks"	,

# "https://sveltetraining.com/blog-articles/the-8-dimensions-of-wellness"	,

# "https://sveltetraining.com/blog-articles/the-8-dimensions-of-wellness"	,

# "https://sveltetraining.com/blog-articles/essential-guidelines-for-working-from-home"	,

# "https://sveltetraining.com/blog-articles/essential-guidelines-for-working-from-home"	,	

# "https://sveltetraining.com/blog-articles/4-reasons-exercising-online-will-help-you-stay-in-line"	,

# "https://sveltetraining.com/blog-articles/4-reasons-exercising-online-will-help-you-stay-in-line"	,	

# "https://sveltetraining.com/blog-articles/weights-do-they-lift-us-toward-our-goal"	,

# "https://sveltetraining.com/blog-articles/weights-do-they-lift-us-toward-our-goal"	,

# "https://sveltetraining.com/contact/"	,

# "https://sveltetraining.com/contact"	,	

# "https://sveltetraining.com/terms/"	,

# "https://sveltetraining.com/terms"	,	

# "https://sveltetraining.com/blog-articles/is-the-liquid-of-life-really-justwater"	,

# "https://sveltetraining.com/blog-articles/is-the-liquid-of-life-really-justwater"	,	

# "https://sveltetraining.com/blog-articles/inflammatory-foods-are-so-last-season"	,

# "https://sveltetraining.com/blog-articles/inflammatory-foods-are-so-last-season"	,

# "https://sveltetraining.com/blog-articles/are-you-breathing-properly"	,

# "https://sveltetraining.com/blog-articles/are-you-breathing-properly"	,

# "https://sveltetraining.com/blog-articles/why-essential-oils"	,

# "https://sveltetraining.com/blog-articles/why-essential-oils"	,	

# "https://sveltetraining.com/blog-articles/does-your-water-brand-matter"	,

# "https://sveltetraining.com/blog-articles/does-your-water-brand-matter"	,	

# "https://sveltetraining.com/blog-articles/social-media-vs-reality"	,

# "https://sveltetraining.com/blog-articles/social-media-vs-reality"	,	

# "https://sveltetraining.com/blog-articles/his-and-her-weight-loss-drive"	,

# "https://sveltetraining.com/blog-articles/his-and-her-weight-loss-drive"	,

# "https://sveltetraining.com/blog-articles/why-hiit-can-hit-you-hard"	,

# "https://sveltetraining.com/blog-articles/why-hiit-can-hit-you-hard"	,

# "https://sveltetraining.com/blog-articles/swapping-cocktails-for-mocktails"	,

# "https://sveltetraining.com/blog-articles/swapping-cocktails-for-mocktails"	,	

# "https://sveltetraining.com/blog-articles/4-ways-to-maintain-healthy-habits-with-a-busy-life"	,

# "https://sveltetraining.com/blog-articles/4-ways-to-maintain-healthy-habits-with-a-busy-life"	,	

# "https://sveltetraining.com/blog-articles/lets-swim-away-from-the-calories"	,

# "https://sveltetraining.com/blog-articles/lets-swim-away-from-the-calories"	,	

# "https://sveltetraining.com/blog-articles/confused-on-whether-to-buy-organic-or-not-this-will-help"	,



# "https://sveltetraining.com/blog-articles/confused-on-whether-to-buy-organic-or-not-this-will-help"	,	

# "https://sveltetraining.com/blog-articles/tips-and-tricks-to-a-healthy-lifestyle"	,

# "https://sveltetraining.com/blog-articles/tips-and-tricks-to-a-healthy-lifestyle"	,	

# "https://sveltetraining.com/blog-articles/5-ways-to-meal-prep-properly"	,

# "https://sveltetraining.com/blog-articles/5-ways-to-meal-prep-properly"	,	

# "https://sveltetraining.com/blog-articles/pretty-plants-for-a-healthy-life"	,

# "https://sveltetraining.com/blog-articles/pretty-plants-for-a-healthy-life"	,	

# "https://sveltetraining.com/blog-articles/do-this-not-that-when-eating-out"	,

# "https://sveltetraining.com/blog-articles/do-this-not-that-when-eating-out"	,	

# "https://sveltetraining.com/blog-articles/3-things-most-people-dont-know-about-stretching"	,

# "https://sveltetraining.com/blog-articles/3-things-most-people-dont-know-about-stretching"	,	

# "https://sveltetraining.com/blog-articles/how-to-love-yourself"	,

# "https://sveltetraining.com/blog-articles/how-to-love-yourself"	,	

# "https://sveltetraining.com/blog-articles/category/Tips"	,


# "https://sveltetraining.com/blog-articles/category/Workouts"	,

# "https://sveltetraining.com/blog-articles/category/Workouts"	,	

# "https://sveltetraining.com/blog-articles/tag/lifestyle"	,

# "https://sveltetraining.com/blog-articles/tag/lifestyle"	,	

# "https://sveltetraining.com/blog-articles/tag/health"	,

# "https://sveltetraining.com/blog-articles/tag/health"	,	

# "https://sveltetraining.com/blog-articles/tag/wellness"	,

# "https://sveltetraining.com/blog-articles/tag/wellness"	,	

# "https://sveltetraining.com/blog-articles/tag/tips"	,

# "https://sveltetraining.com/blog-articles/tag/tips"	,	

# "https://sveltetraining.com/blog-articles/tag/inflammation"	,

# "https://sveltetraining.com/blog-articles/tag/inflammation"	,	

# "https://sveltetraining.com/blog-articles/tag/nutrition"	,

# "https://sveltetraining.com/blog-articles/tag/nutrition"	,	

# "https://sveltetraining.com/blog-articles/caffeine-is-it-worth-it"	,

# "https://sveltetraining.com/blog-articles/caffeine-is-it-worth-it"	,	

# "https://sveltetraining.com/blog-articles/3-ways-supplements-may-help"	,

# "https://sveltetraining.com/blog-articles/3-ways-supplements-may-help"	,	

# "https://sveltetraining.com/blog-articles/importance-of-accountability"	,

# "https://sveltetraining.com/blog-articles/importance-of-accountability"	,	

# "https://sveltetraining.com/blog-articles/who-said-chocolate-couldnt-be-a-womans-weight-loss-best-friend"	,

# "https://sveltetraining.com/blog-articles/who-said-chocolate-couldnt-be-a-womans-weight-loss-best-friend"	,	

# "https://sveltetraining.com/blog-articles/lets-spill-some-tea-and-drink-it"	,

# "https://sveltetraining.com/blog-articles/lets-spill-some-tea-and-drink-it"	,	

# "https://sveltetraining.com/blog-articles/6-ways-to-help-menopause"	,

# "https://sveltetraining.com/blog-articles/6-ways-to-help-menopause"	,	

# "https://sveltetraining.com/blog-articles/did-you-choose-a-program-that-fits-you-and-your-goals"	,

# "https://sveltetraining.com/blog-articles/did-you-choose-a-program-that-fits-you-and-your-goals"	,	

# "https://sveltetraining.com/blog-articles/vitamin-deficiency-"	,

# "https://sveltetraining.com/blog-articles/vitamin-deficiency-"	,	

# "https://sveltetraining.com/blog-articles/what-is-inflammation-and-why-is-it-dangerous"	,

# "https://sveltetraining.com/blog-articles/what-is-inflammation-and-why-is-it-dangerous"	,	

# "https://sveltetraining.com/blog-articles/setting-goals-for-weight-loss"	,

# "https://sveltetraining.com/blog-articles/setting-goals-for-weight-loss"	,	

# "https://sveltetraining.com/blog-articles/benefits-of-eating-natural-foods"	,

# "https://sveltetraining.com/blog-articles/benefits-of-eating-natural-foods"	,	

# "https://sveltetraining.com/blog-articles/reducing-belly-fat-tips-and-exercises"	,

# "https://sveltetraining.com/blog-articles/reducing-belly-fat-tips-and-exercises"	,	

# "https://sveltetraining.com/blog-articles/nutrition-is-more-than-counting-calories"	,

# "https://sveltetraining.com/blog-articles/nutrition-is-more-than-counting-calories"	,	

# "https://sveltetraining.com/blog-articles/5-healthy-morning-routines"	,

# "https://sveltetraining.com/blog-articles/5-healthy-morning-routines"	,	

# "https://sveltetraining.com/blog-articles/5-reasons-why-a-strong-neck-is-important"	,

# "https://sveltetraining.com/blog-articles/5-reasons-why-a-strong-neck-is-important"	,	

# "https://sveltetraining.com/blog-articles/mothers-day-special-3-turmeric-bottles"	,

# "https://sveltetraining.com/blog-articles/mothers-day-special-3-turmeric-bottles"	,	

# "https://sveltetraining.com/blog-articles/cbd"	,

# "https://sveltetraining.com/blog-articles/cbd"	,	

# "https://sveltetraining.com/blog-articles"	,

# "https://sveltetraining.com/blog-articles"	,	

# "https://sveltetraining.com/blog-articles/2019/3/11/misty-mountains-me-menex-kt9b2"	,

# "https://sveltetraining.com/blog-articles/2019/3/11/misty-mountains-me-menex-kt9b2"	,	

# "https://sveltetraining.com/blog-articles/free-fitness-tracker"	,

# "https://sveltetraining.com/blog-articles/free-fitness-tracker"	,	

# "https://sveltetraining.com/blog-articles/full-body-fat-burn-ozHTe"	,

# "https://sveltetraining.com/blog-articles/full-body-fat-burn-ozHTe"	,	

# "https://sveltetraining.com/blog-articles/dont-get-caught-eating-one-of-these-4-things-for-breakfast"	,

# "https://sveltetraining.com/blog-articles/dont-get-caught-eating-one-of-these-4-things-for-breakfast"	,	

# "https://sveltetraining.com/blog-articles/blast-away-nail-fungus-in-24-seconds"	,

# "https://sveltetraining.com/blog-articles/blast-away-nail-fungus-in-24-seconds"	,	

# "https://sveltetraining.com/blog-articles/is-working-out-outside-damaging-your-skin"	,

# "https://sveltetraining.com/blog-articles/is-working-out-outside-damaging-your-skin"	,	

# "https://sveltetraining.com/blog-articles/5-secrets-for-flat-tummy"	,

# "https://sveltetraining.com/blog-articles/5-secrets-for-flat-tummy"	,	

# "https://sveltetraining.com/blog-articles/is-oatmeal-good-for-you-QudP6"	,

# "https://sveltetraining.com/blog-articles/is-oatmeal-good-for-you-QudP6"	,	

# "https://sveltetraining.com/blog-articles/what-avocados-do-to-your-body-K2jSH"	,

# "https://sveltetraining.com/blog-articles/what-avocados-do-to-your-body-K2jSH"	,	

# "https://sveltetraining.com/blog-articles/easy-fun-outdoor-abs-workout"	,

# "https://sveltetraining.com/blog-articles/easy-fun-outdoor-abs-workout"	,	

# "https://sveltetraining.com/blog-articles/get-rid-of-turkey-neck-using-this-instead-of-moisturizer"	,

# "https://sveltetraining.com/blog-articles/get-rid-of-turkey-neck-using-this-instead-of-moisturizer"	,	

# "https://sveltetraining.com/blog-articles/the-blame-game"	,

# "https://sveltetraining.com/blog-articles/the-blame-game"	,	

# "https://sveltetraining.com/blog-articles/special-oil-drops-fat-fast"	,

# "https://sveltetraining.com/blog-articles/special-oil-drops-fat-fast"	,	

# "https://sveltetraining.com/blog-articles/never-do-the-plank-if"	,

# "https://sveltetraining.com/blog-articles/never-do-the-plank-if"	,	

# "https://sveltetraining.com/blog-articles/the-truth-about-eggs"	,

# "https://sveltetraining.com/blog-articles/the-truth-about-eggs"	,	
# "https://sveltetraining.com/blog-articles/what-avocados-do-to-your-body",

# "https://sveltetraining.com/blog-articles/what-avocados-do-to-your-body",
# "https://sveltetraining.com/blog-articles/is-oatmeal-good-for-you",
# "https://sveltetraining.com/blog-articles/is-oatmeal-good-for-you",
# "https://sveltetraining.com/blog-articles/4-ways-to-improve-skin-elasticity",

# "https://sveltetraining.com/blog-articles/4-ways-to-improve-skin-elasticity	",
# "https://sveltetraining.com/blog-articles/3-healthy-boundaries-you-should-consider-setting",
# "https://sveltetraining.com/blog-articles/3-healthy-boundaries-you-should-consider-setting",
# "https://sveltetraining.com/blog-articles/6-things-i-wish-id-known-about-fitness-years-ago",

# "https://sveltetraining.com/blog-articles/6-things-i-wish-id-known-about-fitness-years-ago",

# "https://sveltetraining.com/blog-articles/3-reasons-why-a-positive-mindset-is-more-beneficial",

# "https://sveltetraining.com/blog-articles/3-reasons-why-a-positive-mindset-is-more-beneficial",



# "https://sveltetraining.com/blog-articles/how-citrus-can-help-you-lose-weight"	,

# "https://sveltetraining.com/blog-articles/how-citrus-can-help-you-lose-weight"	,	

# "https://sveltetraining.com/blog-articles/tag/supplements"	,

# "https://sveltetraining.com/blog-articles/tag/supplements"	,

# "https://sveltetraining.com/blog-articles/tag/natural"	,

# "https://sveltetraining.com/blog-articles/tag/natural"	,	

# "https://sveltetraining.com/blog-articles/tag/weight+loss"	,

# "https://sveltetraining.com/blog-articles/tag/weight+loss"	,


# "https://sveltetraining.com/blog-articles/tag/goals"	,

# 	,
# "https://sveltetraining.com/home"	,

# "https://sveltetraining.com "	,
# "https://sveltetraining.com/free-resources/nutrition"	,

# "https://sveltetraining.com/free-resources/nutrition"	,	

# "https://sveltetraining.com/free-resources/mindset"	,

# "https://sveltetraining.com/free-resources/mindset"	,

# "https://sveltetraining.com/free-resources"	,

# "https://sveltetraining.com/free-resources"	,	

# "https://sveltetraining.com/free-resources/workouts"	,

# "https://sveltetraining.com/free-resources/workouts"	,

# "https://sveltetraining.com/apply-application"	,

# "https://sveltetraining.com/apply-application"	,
# "https://sveltetraining.com/blog-articles?offset=1627568420554"	,

# "https://sveltetraining.com/blog-articles"	,	

# "http://sveltetraining.com/contact"	,

# "http://www.sveltetraining.com/apply-application/"	,

# "https://sveltetraining.com/oops"	,

# "https://sveltetraining.com/oops"	,

# "https://sveltetraining.com/agree"	,

# "https://sveltetraining.com/agree"	,	

# "https://sveltetraining.com/offer-unavailable"	,	

# "https://sveltetraining.com/info"	,

# "https://sveltetraining.com/info"	,	

# "https://sveltetraining.com/new-affiliate-agreement"	,

# "https://sveltetraining.com/new-affiliate-agreement	"	,

# "https://sveltetraining.com/blog-articles?offset=1613495266543"	,

# "https://sveltetraining.com/blog-articles	"	,

# "https://sveltetraining.com/apply-application/"	,

# "https://sveltetraining.com/apply-application	"	,

# "https://sveltetraining.com/blog-articles?offset=1590768529462"	,

# "https://sveltetraining.com/blog-articles	"	,

# "https://sveltetraining.com/blog-articles?author=5ed158ef52014c68fd4459cb"	,

# "https://sveltetraining.com/blog-articles?author=52fbd2cfe4b06a1592220111"	,

# "https://sveltetraining.com/blog-articles?offset=1626789600255&reversePaginate=true"	,

# "https://sveltetraining.com/blog-articles?offset=1612893275001&reversePaginate=true"	,

# "https://sveltetraining.com/blog-articles?offset=1590768322416&reversePaginate=true"	]


x = [

"https://sveltetraining.com/blog-articles/tag/goals"		,
"https://sveltetraining.com/home"	,

"https://sveltetraining.com"	,
"https://sveltetraining.com/free-resources/nutrition"	,

"https://sveltetraining.com/free-resources/nutrition"	,	

"https://sveltetraining.com/free-resources/mindset"	,

"https://sveltetraining.com/free-resources/mindset"	,

"https://sveltetraining.com/free-resources"	,

"https://sveltetraining.com/free-resources"	,	

"https://sveltetraining.com/free-resources/workouts"	,

"https://sveltetraining.com/free-resources/workouts"	,

"https://sveltetraining.com/apply-application"	,

"https://sveltetraining.com/apply-application"	,
"https://sveltetraining.com/blog-articles?offset=1627568420554"	,

"https://sveltetraining.com/blog-articles"	,	

"http://sveltetraining.com/contact"	,

"http://www.sveltetraining.com/apply-application/"	,

"https://sveltetraining.com/oops"	,

"https://sveltetraining.com/oops"	,

"https://sveltetraining.com/agree"	,

"https://sveltetraining.com/agree"	,	

"https://sveltetraining.com/offer-unavailable"	,	

"https://sveltetraining.com/info"	,

"https://sveltetraining.com/info"	,	

"https://sveltetraining.com/new-affiliate-agreement"	,

"https://sveltetraining.com/new-affiliate-agreement"	,

"https://sveltetraining.com/blog-articles?offset=1613495266543"	,

"https://sveltetraining.com/blog-articles"	,

"https://sveltetraining.com/apply-application/"	,

"https://sveltetraining.com/apply-application"	,

"https://sveltetraining.com/blog-articles?offset=1590768529462"	,

"https://sveltetraining.com/blog-articles"	,

"https://sveltetraining.com/blog-articles?author=5ed158ef52014c68fd4459cb"	,

"https://sveltetraining.com/blog-articles?author=52fbd2cfe4b06a1592220111"	,

"https://sveltetraining.com/blog-articles?offset=1626789600255&reversePaginate=true"	,

"https://sveltetraining.com/blog-articles?offset=1612893275001&reversePaginate=true"	,

"https://sveltetraining.com/blog-articles?offset=1590768322416&reversePaginate=true"	]


for q in x:
    CHECKGTM(q)
