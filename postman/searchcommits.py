#!/usr/bin/env python
# This test tests the search query functionality of the GitHub API by searching commit for every public repo with that has the string "test" in the name
import requests

url = "http://api.github.com/search/commits"

querystring = {"q":"test"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "daba1db6-f924-4601-b5a2-a4fc9db3e59d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
