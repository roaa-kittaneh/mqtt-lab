import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

student_id = "12218444"

while True:
    people = random.randint(1, 10)
    message = f"{student_id} - People Count: {people}"
    client.publish("sensors/people", message)
    print("Published:", message)
    time.sleep(2)
