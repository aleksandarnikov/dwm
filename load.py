import json

import paho.mqtt.client as mqtt
import time
import sys

name = sys.argv[1]

client = mqtt.Client(name)
client.connect("localhost")


def on_publish(client, userdata, result):
    print("data published \n")
    pass


client.on_publish = on_publish

t = time.time()

with open("data.txt", "r") as f:
    while True:
        s = f.readline()
        if s is None:
            break
        x = json.loads(s)
        tt = x["t"]
        while tt > time.time() - t:
            time.sleep(0.001)
        ret = client.publish("dwm/node/" + name + "/uplink/location", json.dumps(x["data"]))
