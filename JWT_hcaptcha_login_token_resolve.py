import requests

url = "https://api.hcaptcha.com/checksiteconfig"

params = {
  'v': "94cdacf",
  'host': "discord.com",
  'sitekey': "a9b5fb07-92ff-493f-86fe-352a2803b3df",
  'sc': "1",
  'swa': "1",
  'spst': "1"
}

headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
  'Accept': "application/json",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua-platform': "\"Linux\"",
  'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  'Content-Type': "text/plain",
  'sec-ch-ua-mobile': "?0",
  'Origin': "https://newassets.hcaptcha.com",
  'Sec-Fetch-Site': "same-site",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://newassets.hcaptcha.com/",
  'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7"
}

response = requests.post(url, params=params, headers=headers)

print(response.json())
# give you an token to use it in the resolve hcaptcha
