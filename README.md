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
  <img width="1108" height="575" alt="Screenshot 2025-11-29 180542" src="https://github.com/user-attachments/assets/2a33a18e-4177-4157-80ee-06eed9fc1919" />
  <img width="976" height="582" alt="Screenshot 2025-11-29 180606" src="https://github.com/user-attachments/assets/e306d70b-4537-4336-b9fa-b4c7f19f91bb" />
  <img width="1111" height="586" alt="Screenshot 2025-11-29 175807" src="https://github.com/user-attachments/assets/b89ae054-9367-4db9-aab3-ae193ea7ba1d" />
  <img width="1110" height="621" alt="Screenshot 2025-11-29 175821" src="https://github.com/user-attachments/assets/32d6afb7-9ba1-4b7a-903c-e7ff32289758" />
  <img width="1166" height="575" alt="Screenshot 2025-11-29 175834" src="https://github.com/user-attachments/assets/543d2cba-b3e7-4b64-ba53-e28b9229cc10" />
  <img width="1075" height="578" alt="Screenshot 2025-11-29 175846" src="https://github.com/user-attachments/assets/4d937486-90d7-462a-a24a-d78464ce51e8" />
  <img width="1111" height="530" alt="Screenshot 2025-11-29 175903" src="https://github.com/user-attachments/assets/5c8e677d-0e1f-4801-97eb-c1dedccb519f" />
  <img width="828" height="620" alt="Screenshot 2025-11-29 175734" src="https://github.com/user-attachments/assets/183b4e9f-6aae-45b5-adcf-2be369a9df1f" />







