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

