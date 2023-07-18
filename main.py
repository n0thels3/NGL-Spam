import requests
import uuid
import sys
import threading
import time

# Hmm real brawser simulation bepass
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "pragma": 'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
    'sec-ch-ua': 'Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows"
}


def spam(message, target):
    data = {
    'username': str(target),
    'question': str(message),
    'deviceId': str(uuid.uuid4()),
    'gameSlug': '',
    'referrer': 'https://l.instagram.com/'
}

    while True:

        r = requests.post(
            url="https://ngl.link/api/submit",
            data=data,
            headers=headers
        )

        print(f"Gotcha rest in peace {r.status_code}")

        if r.status_code == 429:
            print(f'Hmmm, rate limit, wait 20 seconds')
            time.sleep(20)
        
try:
    username = sys.argv[1]
    message = sys.argv[2]
    threads = sys.argv[3]
except:
    print("python main.py <username-ngl> <message> <threads>")
  
for i in range(int(threads)):
    threading.Thread(target=spam, args=(message, username)).start()
spam(message=message, target=username)
