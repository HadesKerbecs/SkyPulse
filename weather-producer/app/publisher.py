import json
import os
import pika
import time
from .config import RABBIT_HOST, RABBIT_PORT, RABBIT_USER, RABBIT_PASS, RABBIT_QUEUE

class RabbitPublisher:
    def __init__(self):
        url = os.getenv("RABBIT_URL")
        self.params = pika.URLParameters(url)
        self._connect()

    def _connect(self):
        for i in range(5):
            try:
                self.conn = pika.BlockingConnection(self.params)
                self.channel = self.conn.channel()
                self.channel.queue_declare(queue=RABBIT_QUEUE, durable=True)
                return
            except Exception as e:
                print(f"RabbitMQ connect failed ({i+1}/5): {e}")
                time.sleep(2)
        raise ConnectionError("Could not connect to RabbitMQ")

    def publish(self, obj: dict):
        try:
            body = json.dumps(obj, default=str)
            self.channel.basic_publish(
                exchange='',
                routing_key=RABBIT_QUEUE,
                body=body,
                properties=pika.BasicProperties(delivery_mode=2)
            )
            print("Published message to queue")
        except:
            print("Connection lost, reconnecting...")
            self._connect()
            self.publish(obj)
