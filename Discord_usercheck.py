import requests
import json

url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"

payload = {
  "username": "obito"
}

headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua-platform': "\"Linux\"",
  'X-Debug-Options': "bugReporterEnabled",
  'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  'sec-ch-ua-mobile': "?0",
  'X-Discord-Timezone': "Asia/Damascus",
  'X-Discord-Locale': "en-GB",
  'Origin': "https://discord.com",
  'Sec-Fetch-Site': "same-origin",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7",
  
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())
