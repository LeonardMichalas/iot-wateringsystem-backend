#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2010-2013 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation
# Copyright (c) 2010,2011 Roger Light <roger@atchoo.org>
# All rights reserved.

# This shows a simple example of waiting for a message to be published.

# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import json
from time import sleep
import random


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)

# Generates a single, composed message object
def generateMsg():
    msg = {
        "sensors": {
            "humidity": str(random.randint(0, 100)),
            "distance": str(random.randint(0, 100)),
            "button": str(random.randint(0, 1))
        },
        "actuators": {
            "led": str(random.randint(0, 1)),
            "pump": str(random.randint(0, 1))
        }
    }
    return json.dumps(msg)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.username_pw_set("cougar", "iot-bootcamp-2019")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("35.205.157.29", 1883, 60)

mqttc.loop_start()

mqttc.subscribe("/iot-bootcamp-2019/admin/devices/test-device/#", qos=2)

while 1:
    # infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device", generateMsg(), qos=2)
    # infot.wait_for_publish()

    # Publish values as single value per topic
    infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device/sensors/humidity", str(random.randint(0, 100)), qos=2)
    infot.wait_for_publish()
    infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device/sensors/level", str(random.randint(0, 100)), qos=2)
    infot.wait_for_publish()
    infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device/sensors/button", str(random.randint(0, 1)), qos=2)
    infot.wait_for_publish()
    infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device/actuators/led", str(random.randint(0, 1)), qos=2)
    infot.wait_for_publish()
    infot = mqttc.publish("/iot-bootcamp-2019/admin/devices/test-device/actuators/pump", str(random.randint(0, 1)), qos=2)
    infot.wait_for_publish()
    sleep(5)
    