def __init__(self):
    import os
    url = os.getenv("RABBIT_URL")
    self.params = pika.URLParameters(url)
    self._connect()
