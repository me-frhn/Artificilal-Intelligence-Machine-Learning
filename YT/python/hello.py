print("hello world")
print("run using shortcut key")

#python -m venv .venv
#the above command is used to make the environment for the python using the terminal

import requests

response = requests.get("https://api.github.com")

print(response.status_code)
print(response.json())
