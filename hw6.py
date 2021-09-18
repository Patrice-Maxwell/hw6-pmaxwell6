import requests
import os
from dotenv import find_dotenv, load_dotenv
import base64
from secrets import *
load_dotenv(find_dotenv())


AUTH_URL= "https://accounts.spotify.com/api/token"


auth_response = requests.post(AUTH_URL,{
    'grant_type': 'client_credentials' , 
    'client_id' : os.getenv("CLIENT_ID") ,
    'client_secret' :os.getenv("CLIENT_SECRET"),

})
auth_response_json = auth_response.json()
access_token = auth_response_json["access_token"]
headers = {
    'Authorization' : 'Bearer {token}'.format(token= access_token)
}
###############################################
BASE_URL= "https://api.spotify.com/v1/browse/new-releases?"

response_json= requests.get(BASE_URL , headers=headers,
params={'limit' : 20})
response_json = response_json.json()

print("10 new releases  on spotify")



for i in range(10):
    try:
        print(response_json["albums"]["items"][i]['name'] )
    except:
        print("Your code is booty <Smiley Face>")
        break