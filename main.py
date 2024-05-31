import requests
from requests.structures import CaseInsensitiveDict
import random
import time
import json

def get_access_token():
    url = 'https://api.tapswap.ai/api/account/login'
    headers = {
        'Host': 'api.tapswap.ai',
        'Content-Type': 'application/json',
        'X-Cv': '608',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Accept-Language': 'en-GB,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Sec-Fetch-Mode': 'cors',
        'Origin': 'https://app.tapswap.club',
        'X-App': 'tapswap_server',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
        'Referer': 'https://app.tapswap.club/',
        'Content-Length': '505',
        'Sec-Fetch-Dest': 'empty',
        'Connection': 'keep-alive'
    }

    payload = {
        "init_data": "query_id=AAEDr20KAwAAAAOvbQrUk15x&user=%7B%22id%22%3A6617411331%2C%22first_name%22%3A%22Nafis%22%2C%22last_name%22%3A%22Fuad%22%2C%22language_code%22%3A%22en%22%2C%22allows_write_to_pm%22%3Atrue%7D&auth_date=1717005868&hash=82ea1cdb684c00cadef64d8fdb0c8749a6f5a27f2c88e8f97c1a06bfc83e509a",
        "referrer": "",
        "bot_key": "app_bot_2"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        response_json = response.json()
        return response_json.get('access_token')
    else:
        print(f"Failed to get access token, status code: {response.status_code}")
        return None

# Initial access token
access_token = get_access_token()

if access_token:
    for i in range(9999999):
        ran = random.randint(980, 1000)
        url = "https://api.tapswap.ai/api/player/submit_taps"
        
        headers = CaseInsensitiveDict()
        headers["Host"] = "api.tapswap.ai"
        headers["Content-Type"] = "application/json"
        headers["X-Cv"] = "608"
        headers["Accept"] = "*/*"
        headers["Authorization"] = f"Bearer {access_token}"
        headers["Content-Id"] = "22997"
        headers["Sec-Fetch-Site"] = "cross-site"
        headers["Accept-Language"] = "en-GB,en;q=0.9"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Origin"] = "https://app.tapswap.club"
        headers["User-Agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
        headers["Referer"] = "https://app.tapswap.club/"
        headers["X-App"] = "tapswap_server"
        headers["Content-Length"] = "33"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Connection"] = "keep-alive"
        
        data = json.dumps({"taps": ran, "time": 1717006045113})
        
        resp = requests.post(url, headers=headers, data=data)

        if resp.status_code == 401:
            print("Unauthorized, getting new access token...")
            access_token = get_access_token()
            if not access_token:
                print("Failed to get a new access token, exiting...")
                break
        else:
            print("\nCOINS ADDED >>> " + str(ran) + "\n")
            print(resp.text)
            time.sleep(250)
else:
    print("Initial access token fetch failed, exiting...")
