import requests,json,regex

########################################
#Created By Hansen Gianto
#Instagram Profile Data Scraper
########################################

username = "hansen_gianto"
r = requests.get(f"https://instagram.com/{username}", timeout=10).text

pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
find = pattern.findall(r)

db = json.loads(find[4])

print(json.dumps(db["entry_data"]["ProfilePage"][0]["graphql"]["user"], indent=4, sort_keys=True))
