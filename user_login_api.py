import requests

# send bad login to hackthissite.org

# payload: 
payload = {'username':'testuser', 'password':'password'}
url = 'https://www.hackthissite.org/user/login'

# make the request: 
req = requests.post(url, data=payload)

# check the response code
print(req.status_code)
# check the response content
print(req.text)