import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

student_id = "12218444"

while True:
    temperature = random.randint(20, 30)
    message = f"{student_id} - Temperature: {temperature}"
    client.publish("sensors/temperature", message)
    print("Published:", message)
    time.sleep(2)
