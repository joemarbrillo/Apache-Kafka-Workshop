# This is my Apache Kafka Workshop

Learning reference: 
https://www.youtube.com/watch?v=Lb5UDslK6ZE

## Plan: 
1. Kafka basics (brokers, topics, partitions, offsets, KRaft)
2. Run one Kafka node locally, and use thecommand line tools.
3. Producers and consumers in Python, with JSON events and schema
4. Keys, delivery guarantees, consumer groups and offsets
5. Errors: validation nand a dead-letter topic
6. Stream processing consume, tranform, produce, exactly once
7. Project: live orders -> Spark structured streaming -> Parquet -> report

## Download Kafka:
https://archive.apache.org/dist/kafka/4.4.0/kafka_2.13-4.4.0.tgz

> pip install confluent-kafka==2.16.1 pyspark==4.3.0

> python -c "import confluent_kafka, pyspark; print(confluent_kafka.version(), pyspark.__version__)"
2.16.1 4.3.0

Get the Kafka connectors dependencies:
> python get_jars.py

## Run in terminal
Requires pip install ipykernel
> papermill set_kafka_path.ipynb output_set_kafka_path.ipynb


## Check the Kafka status
> kafka-metadata-quorum.sh --bootstrap-server $BS describe --status

## Setup a local (docker) kafka container:
> docker run -d --name broker -p 9092:9092 apache/kafka:latest

## Set the broker:
Every time you run docker exec, it starts a fresh shell without your previous export variables.
> set PATH="$PWD/kafka/bin:$PATH"
> set "BS=localhost:9092"
Or, export for command terminal use


## Open the broker shell terminal:
> docker exec --workdir /opt/kafka/bin/ -it broker sh


## Create a topic
> ./kafka-topics.sh --bootstrap-server $BS --create --topic hello --partitions 1
Created topic hello.


> ./kafka-topics.sh --bootstrap-server $BS --list
__consumer_offsets
hello


> ./kafka-topics.sh --bootstrap-server $BS --describe --topic hello
Topic: hello    TopicId: 2nAJpiVgRh23zcJu5xLu7A PartitionCount: 1       ReplicationFactor: 1    Configs: min.insync.replicas=1,segment.bytes=1073741824
        Topic: hello    Partition: 0    Leader: 1       Replicas: 1     Isr: 1  Elr:    LastKnownElr:


> printf "first event\nsecond event\nthird event\s" | ./kafka-console-producer.sh --bootstrap-server $BS --topic hello


## Read it with a console consumer
> ./kafka-console-consumer.sh --bootstrap-server $BS --topic hello --from-beginning --max-messages 3
The consumer rebalance protocol (KIP-848) is production-ready! Set group.protocol=consumer to try it out. See https://kafka.apache.org/documentation/#consumer_rebalance_protocol
first event
second event
third event\s
Processed a total of 3 messages


## See where each event lives:
> ./kafka-console-consumer.sh --bootstrap-server $BS --topic hello --from-beginning --max-messages 3 --formatter-property print.partition=true --formatter-property print.offset=true
The consumer rebalance protocol (KIP-848) is production-ready! Set group.protocol=consumer to try it out. See https://kafka.apache.org/documentation/#consumer_rebalance_protocol
Partition:0     Offset:0        first event
Partition:0     Offset:1        second event
Partition:0     Offset:2        third event\s
Processed a total of 3 messages


> ./kafka-get-offsets.sh --bootstrap-server $BS --topic hello
hello:0:3


## Debugging and testing:


## Create a topic with 3 partitions
> kafka-topics.sh --bootstrap-server $BS --create --topic keys-demo --partitions 3


