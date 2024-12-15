import requests

# API URL and Key
url = "https://api.meraki.com/api/v1/networks/L_784752235069309716/wireless/ssids/1"  # Endpoint for SSID number 1
api_key = "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6"

# Request headers
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Payload to enable the SSID
payload = {
    "enabled": True
}

# Sending the PUT request
response = requests.put(url, headers=headers, json=payload)

# Checking and printing the response
if response.status_code == 200:
    print("SSID successfully enabled.")
    print(response.json())  # Print updated SSID configuration
else:
    print(f"Failed to enable SSID. Status code: {response.status_code}")
    print(response.text)  # Print the error message
