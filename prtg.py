import requests
import getpass
import xmltodict
import pprint

# Supress HTTPS Warnings
requests.urllib3.disable_warnings()

#server = input('Server: ')
#username = input('Username: ')
#password = getpass.getpass()

server = 'p'
username = ''
password = ''
passhash = ''
device_id = input("Device ID: ")

creds = '&username=' + username + '&passhash=' + passhash

#creds = {'server': server,
#    'username': username,
#    'password': password,
#    'pass_hash': pass_hash,}


def prtg_clone_uptime(server,device_id,creds):
    url = 'https://' + server + '/api/duplicateobject.htm?id=44684&name=SNMP%20System%20Uptime&targetid=' + device_id + creds
    response = requests.post(url, verify=False)
    print(response)


def prtg_set_geo(server,device_id,creds):
    url = 'https://' + server + '/api/setlonlat.htm?id=' + device_id + '&location=ADDRESS&lonlat=-84.00,39.00'  + creds
    response = requests.post(url, verify=False)
    print(response)


def prtg_rename_device(server,device_id,creds):
    url = 'https://' + server + '/api/table.xml?content=sensortree&id=' + device_id + '&name' + creds
    response = requests.post(url, verify=False)
    response = (response.text)
    response_dict = xmltodict.parse(response)
    name = response_dict['prtg']['sensortree']['nodes']['device']['name']
    new_name = name + ' [' + device_id + ']'
    url = 'https://' + server + '/api/rename.htm?id=' + device_id + '&value=' + new_name + creds
    response = requests.post(url, verify=False)
    print(response)


prtg_clone_uptime(server,device_id,creds)
prtg_set_geo(server,device_id,creds)
prtg_rename_device(server,device_id,creds)
