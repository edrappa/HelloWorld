from flask import Flask
from datetime import datetime
import os

version = "0.0.1"
start = None


def custom_call():
    global start
    start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class MyFlaskApp(Flask):
  def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
      with self.app_context():
        custom_call()
    super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)


app = MyFlaskApp(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    return 'Hello!'


@app.route('/healthz', methods=["GET"])
def health_status():
    response = {
        "status": "OK",
        "version": version,
        "uptime": f"up since {start}"
    }
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
