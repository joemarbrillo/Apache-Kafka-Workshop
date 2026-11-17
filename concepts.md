# Kafka in six words

- Event: a fact that happened, key + value + timestamp
- Broker: one Kafka server. A cluster is several brokers sharing the work.
- Topic: a name stream of an event, like a table name. Append only. In this workshop is "orders"
- Partition: a topic is split into partitions, so many machines can share it.
- Offset: position of an event in its partition, like a line number: 0, 1, 2...
- Consumer group: consumers with the same group id share the partitions of a topic.

Bonus:
KRaft - Kafka stores its own metadate in a Kafka log. No ZooKeeper since Kafka 4.0.

Hot key - key with far more events than the other, that could overload other partitions.

linger.ms - improves throughput waits for few ms to process bigger workloads

enable.idempotence - prevent duplication


--dry-run: shows the neew offsets

