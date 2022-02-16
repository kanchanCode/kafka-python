# kafka-python
Python Version 3.8.10 Kafka Version 2.13-3.1.0

Sending messages from producer to consumer using python code for consumer as well as producer Kafka makes use of a tool called ZooKeeper which is a centralized service for a distributed environment like Kafka. It offers configuration service, synchronization service, and a naming registry for large distributed systems.

Thus, we need to first start the ZooKeeper server followed by the Kafka server. This can be achieved using the following commands:

Start ZooKeeper Server
./bin/zookeeper-server-start.sh config/zookeeper.properties

Start Kafka Server
./bin/kafka-server-start.sh config/server.properties

Starting kafka topics : Let us start by creating a python-kafka-test Kafka topic with a single partition and replica. This can be done using the following command:./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 2 --topic python-kafka

Now, let us list down all of our Kafka topics to check if we have successfully created our sample topic. We can make use of the list command here: bin/kafka-topics.sh --list --bootstrap-server localhost:9092

Now Creating a producer :(here we use broker-list) $ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic python-kafka

In another terminal go to kafka(cd $KAFKA_HOME)and create consumer Creating a consumer :(here for consumer we use bootstrap-server) $ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic python-kafka --from-beginning

The run your producer code and check the data on consumer side terminal
