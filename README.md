# MQTT Lab

## What I did
- Installed mosquitto broker (local).
- Implemented 3 publishers: temperature, humidity, people_counter (Python, paho-mqtt).
- Implemented subscribers: one per topic + combined subscriber.
- All messages include `student_id`.

## How to run
1. Start broker: `mosquitto -v`
2. Start publishers and subscribers as listed in `run.sh`.

## Results
- Logs in `logs/` — see `pub_temp.log`, `sub_temp.log`...
  

