from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('python-kafka',b'Hello World')
producer.send('python-kafka',b'This is Kafka-Python, Here we are using only single broker')
producer.flush()
