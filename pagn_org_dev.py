import requests
import argparse
import json
from rich import print

BASE_URL = "https://api.meraki.com/api/v1/organizations/1215707/devices"
API_KEY = "75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6"

def fetch_devices(per_page, starting_after=None, ending_before=None):
    params = {"perPage": per_page}
    if starting_after:
        params["startingAfter"] = starting_after
    if ending_before:
        params["endingBefore"] = ending_before

    response = requests.get(BASE_URL, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }, params=params)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--perPage", type=int, required=True)
    parser.add_argument("--startingAfter", type=str)
    parser.add_argument("--endingBefore", type=str)
    args = parser.parse_args()

    fetch_devices(args.perPage, args.startingAfter, args.endingBefore)

if __name__ == "__main__":
    main()
    
    
####RUN the command in any of the following ways
# '''
# python3 pagination.py --perPage=5
# python3 pagination.py --perPage=5 --startingAfter=QBSA-AY83-4RUF
# python3 pagination.py --perPage=5 --endingBefore=QBSD-VL75-6P62
# '''
