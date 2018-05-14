#!/usr/bin/env python
# This test tests the search query functionality of the GitHub API by searching for every public repo with that has the string "testapi" in the name

import requests

url = "https://api.github.com/search/repositories"

querystring = {"q":"testapi"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "1bc31f90-9e51-41b4-b7ef-a0e416c59dd9"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
