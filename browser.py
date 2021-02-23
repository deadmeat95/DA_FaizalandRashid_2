# Use the Request library
import requests
# Set the target webpage
url = 'https://home.cern/'
r = requests.get(url)
# This will get the full page
print(r.text)
# This will get the status code
print("Status code:")
print("\t *", r.status_code)
print("OK")
# This will just get just the headers
h = requests.head(url)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
#This will modify the header user agent
headers = {
    'User-Agent': 'Mobile'
}
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)

