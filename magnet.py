import shutil
import tempfile
import os.path as pt
import sys
import libtorrent as lt
from time import sleep
import json
import requests 
import multiprocessing
from Magnet_To_Torrent2 import magnet2torrent

jobs = []
count = 0
page = 0
for i in range(0, 10000):

    if page == 0:
        url = "https://nyaa.pantsu.cat/api"
        response = requests.get(url)
        data = json.loads(response.text)
        for i in data["torrents"]:
            path = "torrents/" + i["hash"].lstrip()+".torrent"
            if pt.isfile(path):
                print("file exists")
            else:
                count += 1
                p = multiprocessing.Process(target=magnet2torrent, args=(i["magnet"]+"&tr=http://nyaa.tracker.wf:7777/announce&tr=http://anidex.moe:6969/announce", path))
                jobs.append(p)
                p.start()
    else:
        print(i)
        url = "https://nyaa.pantsu.cat/api/" + str(i)
        response = requests.get(url)
        data = json.loads(response.text)
        for i in data["torrents"]:
            path = "torrents/" + i["hash"].lstrip()+".torrent"
            if pt.isfile(path):
                print("file exists")
            else:
                count += 1
                print("Worker %i", count)
                p = multiprocessing.Process(target=magnet2torrent, args=(i["magnet"]+"&tr=http://nyaa.tracker.wf:7777/announce&tr=http://anidex.moe:6969/announce", path))
                jobs.append(p)
                p.start()
    page += 1
    sleep(1)
print("finished")
sys.exit(0)

