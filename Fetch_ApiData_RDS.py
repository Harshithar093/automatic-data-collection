import json
import requests
import psycopg2
from datetime import datetime


def lambda_handler(event, context):
    conn = psycopg2.connect(database="test", user="postgres", password="postgres", host="localhost", port="5432")
    cur = conn.cursor()
    url = "http://api.open-notify.org/iss-now.json"
    try:

        response_API = requests.get(url)
        data = response_API.text
        result = json.loads(data)

        location = result["iss_position"]
        latitude = location['latitude']
        longitude = location['longitude']
        timestamp = result["timestamp"]
        latitude = float(latitude)
        longitude = float(longitude)
        iss_time = datetime.fromtimestamp(timestamp)
        cur.execute("INSERT INTO iss_table VALUES(%s, %s, %s )", (latitude, longitude, iss_time))
        output = cur.execute("select * from iss_table")
        conn.commit()
        cur.close()

    except IOError as io:
        print("ERROR!")

