import requests
from rich import print


url = "https://api.meraki.com/api/v1/networks/L_784752235069309716/wireless/ssids"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())
