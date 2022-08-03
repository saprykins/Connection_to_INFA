import requests
import json


# psw management
from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method



# GET CREDENTIALS FOR INFA

import os 
user_name = os.environ.get('USER')
user_password = os.environ.get('PASSWORD')



# LOGIN TO INFA

# is used to get icSessionId
url = 'https://dm-em.informaticacloud.com/ma/api/v2/user/login'

myobj = {
    "@type":"login",
    "username":user_name,
    "password": user_password
}

# x is response from INFA
x = requests.post(url, json = myobj)
# make response as json to be able to read as dictionary
json_obj = x.json()

# informatica session id
session_id = json_obj["icSessionId"]
print(session_id)



# START A TASK

url_job = 'https://emw1.dm-em.informaticacloud.com/saas/api/v2/job'
Headers = {"icSessionId": session_id}

myobj = {
    "@type":"job",
    "taskId":"0119EH0I000000000002",
    "taskType":"DSS"
}

y = requests.post(url_job, headers=Headers, json = myobj)
print(y)



# CLOSE SESSION

url_logout = "https://dm-em.informaticacloud.com/ma/api/v2/user/logout"

myobj = {
    "@type":"logout"
}
z = requests.post(url_logout, json = myobj)
print(z)



# TO GO FURTHER

# make json beautiful 
# https://www.journaldev.com/33302/python-pretty-print-json

