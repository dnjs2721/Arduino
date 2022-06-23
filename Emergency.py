import posturl
import requests, json

def SOS():
    data = json.dumps({ 
        'helmetId' : 'H0001'
        })
    header = {'Content-type' : 'application/json'}
    res = requests.post(posturl.sos(), data=data, headers=header)
