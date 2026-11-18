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

What's a poison-pill?
An event that crashes the consumer every time, so the consumer can never get passed.

Why do we keep the original key-value?
So nothing is lost, it can be replayed.

Why flush the dead-letter producer before committing?
If we commit first and then crash, the bad event will be neither processed or saved.

Checkpoints - describes one query's progress.

Why partition the lake by date - can skip all day's folder.

Watermark: 

Kafka - a distributed, durable, append-only event log, producers write events to topics. Consumers read at their own pace, until retention removes them.

Kafka vs Traditional message queue. A queue usually deletes once it is consumed, but Kafka retains it until it's retention policy is met.

How Kafka guatantees ordering. Only within a partition, order with the same key, always go to the same partition.

What's a consumer group? Consumers sharing a group ids split the partition a topic within them.

What happens during a rebalance?

