#!/usr/local/bin/python3
import urllib.request
import urllib.parse
import json

jukebox_url = 'http://jukebox.bink.com'

def get_state():
    url = f"{jukebox_url}/state"
    f = urllib.request.urlopen(url)
    active = f.read().decode('utf-8').rstrip()
    return active

def get_stations():
    url = f"{jukebox_url}/station"
    f = urllib.request.urlopen(url)
    stations = json.loads(f.read().decode('utf-8'))
    return stations

def print_stations(stations):
    for station,info in stations.items():
        print(f"{info['friendly_name']} |terminal=false refresh=true image={info['icon']} bash=/usr/bin/curl param1={jukebox_url}/station/{station}")

active = get_state()
stations = get_stations()

if active in stations:
    status_icon = stations[active]['icon']
    active_name = stations[active]['friendly_name']
else:
    status_icon = None
    active_name = active

if status_icon:
    print(f"{active_name}|image={status_icon}")
else:
    print(f":radio:{active_name}")
print('---')
print('Stations:')
print_stations(stations)
