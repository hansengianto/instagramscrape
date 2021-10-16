import requests,json,regex

########################################
#Created By Hansen Gianto
#Instagram Post Data Scraper
########################################

r = requests.get("https://www.instagram.com/p/CUtRouDBUlG/").text

pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
cari = pattern.findall(r)

db = json.loads(cari[4])

print(json.dumps(db["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"], indent=4, sort_keys=True))
