#!/usr/bin/env python
# This tests performs a paginated  search query limited to two pages  of the GitHub API by searching for every public repo with that has the string "testapi" in the name


import requests

url = "https://api.github.com/search/repositories"

querystring = {"q":"testapi","page1":"","per_page":"2"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "794d3420-196b-4c10-87de-50d3aff8c6de"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
