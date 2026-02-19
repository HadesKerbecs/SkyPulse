import time
import logging
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from apscheduler.schedulers.blocking import BlockingScheduler
from .fetcher import fetch_open_meteo
from .publisher import RabbitPublisher
from .config import INTERVAL_MINUTES

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


def start_http():
    import os
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


def job():
    try:
        weather = fetch_open_meteo()
        data = weather.dict()
        publisher.publish(data)
    except Exception as e:
        logging.exception("Erro no job de coleta/publicação: %s", e)


if __name__ == "__main__":

    threading.Thread(target=start_http, daemon=True).start()

    publisher = RabbitPublisher()
    scheduler = BlockingScheduler()

    job()
    scheduler.add_job(job, 'interval', minutes=INTERVAL_MINUTES)

    try:
        logging.info("Iniciando scheduler...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logging.info("Encerrando serviço")
