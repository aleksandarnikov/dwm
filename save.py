import time
import paho.mqtt.client as mqtt
import json

global t
global f
global writes
writes = 0
f = None
t = time.time()


def on_message(client, userdata, message):
    global t
    global f
    global writes
    m = json.loads(str(message.payload.decode("utf-8")))
    print(m)
    if f is not None:
        if writes == 100:
            writes = 0
            f.close()
            f = None

    if f is None:
        f = open("data.txt", "a+")

    writes = writes + 1
    f.write(json.dumps({"t":time.time() - t, "data": m}) + "\n")


def conn():
    client = mqtt.Client("SAVE1")
    # client.connect("172.20.10.14")
    client.connect("localhost")
    client.on_message = on_message
    # client.subscribe("dwm/node/+/uplink/location")
    client.subscribe("dwm/node/+/uplink/#")
    client.loop_start()
    #time.sleep(60)


def save():
    while True:
        time.sleep(60)


conn()
save()