import requests
data=requests.get("https://www.heroku.com/")
print(data.text)