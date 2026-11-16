#!/bin/bash

# Start or one-node kafka (KRaft) in the background and wait until it answers.
cd "$(dirname "$0")"
if [ ! -d kafka-data ]; then
    kafka/bin/kafka-storage.sh format --standalone -c kafka.properties \
        -t "$(kafka/bin/kafka-storage.sh random-uuid)"
fi

export KAFKA_HEAP_OPTS="-Xmx512m -Xms512m"
kafka/bin/kafka-server-start.sh -daemon kafka.properties

until kafka/bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092 \
    > dev/null 2>&1; do sleep 1; done

echo "Kafka is up on localhost:9092"
