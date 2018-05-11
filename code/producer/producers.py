import os
from kombu import Connection, Producer
from .queues import exchange


def transport_task(key, queue, args=(), kwargs={}):
    # payload that will be sent to broker
    payload = {
        'args': args,
        'kwargs': kwargs,
    }

    # retry policy for declaring the queue
    retry_policy = {
        'interval_start': 0,
        'interval_step': 2,
        'interval_max': 60,
        'max_retries': 30
    }

    with Connection(os.environ.get('BROKER_URL')) as connection:
        with connection.channel() as channel:
            producer = Producer(channel)
            producer.publish(
                payload,
                retry=True,
                retry_policy=retry_policy,
                exchange=exchange,
                routing_key=queue.routing_key,
                declare=[queue]
            )
            producer.release()
