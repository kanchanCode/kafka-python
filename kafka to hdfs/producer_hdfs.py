import csv
import requests
import os
from kafka import KafkaProducer
from json import dumps

from decouple import config


bootstrap_servers=['localhost:9092']
producer = KafkaProducer(value_serializer=lambda K:dumps(K).encode('utf-8'))

key = config('KEY')

CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=1min&slice=year1month1&apikey= key'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        producer.send('topic_hdfs',row)
