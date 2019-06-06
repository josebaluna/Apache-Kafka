<a href="https://kafka.apache.org/"><img src="https://kafka.apache.org/images/logo.png" width="325" height="97"></a><br>

# Producers to upload the observe measurements and consumers <br>

## Apache Kafka Quick Start <br>

**.	Download lasted binary reléase: https://kafka.apache.org/downloads.**<br>
**.	Extract: Unix: $ tar -xzf kafka_2.12-2.2.0.tgz.**<br>
**.	Open a console.**<br>
**.	$ cd kafka_2.12-2.2.0.**<br>


## Start Apache Zookeeper

**.	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0.**<br>
**.	Start: $ bin/zookeeper-server-start.sh config/zookeeper.properties.**<br>



## Start a Kafka Broker

**.	Open a new console.**<br>
**.	$ cd kafka_2.12-2.2.0.**<br>
**.	$ bin/kafka-server-start.sh config/server.properties.**<br>
**.	$ bin/kafka-server-start.sh config/server-1.properties .**<br>

## Edit the following properties of config/server-1.properties:

**.	broker.id=1 # The id of the broker. .**<br>
**.	listeners=PLAINTEXT://:9093 # Port andsecurity of the Broker (PLAINTEXT – no security) .**<br>
**. log.dirs=/tmp/kafka-logs-1 # Directory for new Broker data .**<br>


## Kafka create topic

**.	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0 .**<br>
**.	$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092,localhost:9093 -- replication-factor 2 --partitions 2 --topic 
bigdataroom .**<br>
**.	Let’s check the topic’s been created:  $ bin/kafka-topics.sh --list --bootstrap-server localhost:9092 .**<br>


## Kafka example consumer 

**.	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0 .**<br>
**.	$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bigdataroom --from-beginning .**<br>


## Kafka example producer 

**.	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0 .**<br>
**.	$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic bigdataroom .**<br>
