import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("localhost", 1883, 60)

student_id = "12218444"

while True:
    humidity = random.randint(40, 80)
    message = f"{student_id} - Humidity: {humidity}"
    client.publish("sensors/humidity", message)
    print("Published:", message)
    time.sleep(2)
