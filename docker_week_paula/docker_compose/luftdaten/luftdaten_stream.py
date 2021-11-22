import requests
import time

SENSOR_URL = "http://api.luftdaten.info/static/v1/sensor/{}/"

webhook_url = "https://hooks.slack.com/services/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"



def pick_luftdaten_values(sensor_id):
    result = requests.get(SENSOR_URL.format(sensor_id))
    data = result.json()
    time_stamp = data[0]['timestamp']
    PM25 = data[0]['sensordatavalues'][0]['value']
    PM10 = data[0]['sensordatavalues'][1]['value']
    return time_stamp, PM25, PM10


if __name__ == '__main__':
    while True:
        time_stamp, PM25, PM10 = pick_luftdaten_values(21124)
        text_slack = f'Air quality data at {time_stamp}: PM25 = {PM25}, PM10 = {PM10}'
        data = {'text':text_slack}
        requests.post(url = webhook_url, json = data)
        time.sleep(500)