from kafka import KafkaConsumer
import os
import sys


consumer = KafkaConsumer('topic_hdfs',auto_offset_reset = 'earliest',group_id = None,
                    )


with open('stock.txt','w') as f:
    for message in consumer:
        values = message.value
        values = str(values)
        f.write(values)
        f.write('\n')
        print(values)
sys.stdout.close()
