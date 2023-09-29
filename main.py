import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "password"
GRAPH_ID = "graphusername"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

##Kreirao sam user-a
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding graph",
    "unit": "minute",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixal_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity": input("How manu minutes do you coding? "),
}

pixal_headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=pixel_endpoint, json=pixal_config, headers=pixal_headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "550",
}

# response = requests.put(url=update_endpoint, json=update_config, headers=pixal_headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=pixal_headers)
# print(response.text)