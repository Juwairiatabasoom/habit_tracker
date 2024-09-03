import requests
from datetime import datetime

##setting up user account on pixela
USER_NAME="juwairiatabasoom"
TOKEN="juwairiatabasoom"
PIXELA_ENDPOINT="https://pixe.la/v1/users"
user_params={"token":"juwairiatabasoom",
             "username":"juwairiatabasoom",
             "agreeTermsOfService":"yes",
             "notMinor":"yes"}

# response=requests.post(PIXELA_ENDPOINT,json=user_params)

GRAPH_ID="graph1"
Graph_endpoint=f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
GRAPH_PARAMS={"id":"graph1",
    "name":"DSA graph",
    "unit":"num of ques",
    "type":"int",
    "color":"sora"
}

headers={
    "X-USER-TOKEN": TOKEN
}

#response=requests.post(url=Graph_endpoint,json=GRAPH_PARAMS,headers=headers)

##############################################################################POSTING PIXELS################################################################################

today=datetime.now()

PIXEL_CREATION_ENDPOINT=f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many DSA questions did you do today? ")
}

response=requests.post(url=PIXEL_CREATION_ENDPOINT,json=pixel_data,headers=headers)

##############################################################################UPDATING PIXELS####################################################################################
update_pixel_endpoint=f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
UPDATE_DATA={"quantity":"1"}
# response=requests.put(url=update_pixel_endpoint,json=UPDATE_DATA,headers=headers)

#DELETING A PIXEL
DELETE_PIXEL=f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response=requests.delete(url=DELETE_PIXEL,headers=headers)
