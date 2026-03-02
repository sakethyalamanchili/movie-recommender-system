"""Kafka stream consumer — ingests watch/rate events.

TODO (M2): Full implementation with schema validation and Parquet writes.
"""

import os
from confluent_kafka import Consumer


def create_consumer() -> Consumer:
    """Create a configured Kafka consumer."""
    return Consumer({
        "bootstrap.servers": os.environ["KAFKA_BOOTSTRAP"],
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": os.environ["KAFKA_API_KEY"],
        "sasl.password": os.environ["KAFKA_API_SECRET"],
        "group.id": os.environ.get("KAFKA_GROUP", "ingestor"),
        "auto.offset.reset": "earliest",
    })


def run_consumer():
    """Main consumer loop: poll → validate → write → commit."""
    consumer = create_consumer()
    topics = [os.environ["WATCH_TOPIC"], os.environ["RATE_TOPIC"]]
    consumer.subscribe(topics)

    print(f"Subscribed to: {topics}")

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            # TODO (M2):
            # 1. Deserialize with Avro schema
            # 2. Validate with pandera
            # 3. Write to Parquet snapshot
            # 4. Optionally update Redis cache
            print(f"Received: topic={msg.topic()} partition={msg.partition()} offset={msg.offset()}")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    run_consumer()
