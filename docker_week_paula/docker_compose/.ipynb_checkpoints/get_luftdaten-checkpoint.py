import requests
import json
import random
import time
import logging 

SENSOR_URL = "http://api.luftdaten.info/static/v1/sensor/{}/"

def pick_luftdaten_values(sensor_id):
    # Sensordaten für Luftdaten (p1/p2=Feinstaubwerte, DHT für Temp und Luftfeuchte) abfragen
    # dazu die api von luftdaten.info nutzen
    result = requests.get(SENSOR_URL.format(sensor_id))
    data = result.json()
    time = data[0]['timestamp']
    P1 = data[0]['sensordatavalues'][0]['value']
    P2 = data[0]['sensordatavalues'][1]['value']
    lon = data[0]['location']['longitude']
    lat = data[0]['location']['latitude']
    return time, PM25, PM10, lon, lat

sensors_stuttgart = [1625, 2023, 7037]

while True:
    sensor_id = random.choice(sensors_stuttgart)
    t_stamp, PM25, PM10, lon, lat  = pick_luftdaten_values(1625)
    #print(f'sensor data for sensor {sensor_id}: PM 2.5 {PM25}, PM 10 {PM10}, time {t_stamp}')
    logging.critical(f'sensor data for sensor {sensor_id}: PM 2.5 {PM25}, PM 10 {PM10}, time {t_stamp}')
    time.sleep(30)
