import pygame
import time
import paho.mqtt.client as mqtt
import json

global coords
coords = dict()


def on_message(client, userdata, message):
    global coords
    # print("message received ", str(message.payload.decode("utf-8")))
    # print("message topic=", message.topic)
    m = json.loads(str(message.payload.decode("utf-8")))
    t = message.topic.split("/")[2]
    pos = dict()
    pos["x"] = float(m["position"]["x"])
    pos["y"] = float(m["position"]["y"])
    coords[t] = pos


def conn():
    client = mqtt.Client("GUI1")
    # client.connect("172.20.10.14")
    client.connect("localhost")
    client.on_message = on_message
    # client.subscribe("dwm/node/+/uplink/location")
    client.subscribe("dwm/node/+/uplink/#")
    client.loop_start()
    #time.sleep(60)


def game():
    global coords
    pygame.init()
    clock = pygame.time.Clock()
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    colors = [red, green, blue, yellow]
    colordrone = dict()
    colornum = 0

    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.update()
    pygame.display.set_caption('Drone Racing')
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        dis.fill(white)
        coords2 = coords.copy()
        for c in coords2:
            p = coords2[c]
            rect = [int(p["x"] / 10 * dis_width), int(p["y"] / 10 * dis_height), 10, 10]

            if c not in colordrone:
                colordrone[c] = colors[colornum]
                colornum += 1
                colornum %= len(colors)

            pygame.draw.rect(dis, colordrone[c], rect)
        pygame.display.update()


    pygame.quit()
    quit()


conn()
game()
