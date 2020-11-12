import paho.mqtt.client as mqtt
import time
import random
import sys

name = sys.argv[1]

client = mqtt.Client(name)
client.connect("localhost")


def on_publish(client, userdata, result):
    print("data published \n")
    pass


client.on_publish = on_publish

# ret = client.publish("dwm/node/abc1/uplink/location", '{"position":{"x":1.3936733,"y":1.174517,"z":-0.26708269,"quality":81},"superFrameNumber":136}')
x = 5
y = 4
dx = 0.06
dy = 0.05
while True:
    ddx = x + dx
    ddy = y + dy
    if ddx >= 10 or ddx < 0:
        dx = -dx
        continue
    if ddy >= 10 or ddy < 0:
        dy = -dy
        continue
    x = ddx
    y = ddy
    ret = client.publish("dwm/node/" + name + "/uplink/location", '{"position":{"x":' + str(x) + ',"y":' + str(y) + ',"z":-0.26708269,"quality":81},"superFrameNumber":136}')
    print(x, y)
    time.sleep(0.01)

# ret2 = client.publish("abc", "xyz")
client.loop_start()    #start the loop
time.sleep(10)


