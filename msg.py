# install paho
# pip install paho-mqtt

import time

import paho.mqtt.client as mqtt

# Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

client = mqtt.Client("GUI2")
#client.connect("172.20.10.14")
client.connect("localhost")

# publish(topic, payload=None, qos=0, retain=False)

def on_message(client, userdata, message):
    #     if str(message.topic).endswith('location'):
    #         return
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("")
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)

client.on_message = on_message
client.subscribe("+")
# client.subscribe("dwm/node/+/uplink/#")

client.loop_start()    #start the loop

print("started")
time.sleep(60)