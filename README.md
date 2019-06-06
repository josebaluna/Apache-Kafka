<a href="https://kafka.apache.org/"><img src="https://kafka.apache.org/images/logo.png" align="left"></a>

# Producers to upload the observe measurements and consumers

Apache Kafka Quick Start

•	Download lasted binary reléase: https://kafka.apache.org/downloads
•	Extract: Unix: $ tar -xzf kafka_2.12-2.2.0.tgz
•	Open a console
•	$ cd kafka_2.12-2.2.0


Start Apache Zookeeper

•	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0
•	Start: $ bin/zookeeper-server-start.sh config/zookeeper.properties



Start a Kafka Broker

•	Open a new console
•	$ cd kafka_2.12-2.2.0
•	$ bin/kafka-server-start.sh config/server.properties
•	$ bin/kafka-server-start.sh config/server-1.properties 

Edit the following properties of config/server-1.properties: 
•	broker.id=1 # The id of the broker. It is unique 
•	listeners=PLAINTEXT://:9093 # Port andsecurity of the Broker (PLAINTEXT – no security) 
•	log.dirs=/tmp/kafka-logs-1 # Directory for new Broker data 


Kafka create topic

•	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0
•	$ bin/kafka-topics.sh --create --bootstrap-server localhost:9092,localhost:9093 -- replication-factor 2 --partitions 2 --topic bigdataroom
•	Let’s check the topic’s been created:  $ bin/kafka-topics.sh --list --bootstrap-server localhost:9092 


Kafka example consumer 

•	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0
•	$ bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bigdataroom --from-beginning 


Kafka example producer 

•	Open a terminal and go to the folder: $ cd kafka_2.12-2.2.0
•	$ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic bigdataroom
