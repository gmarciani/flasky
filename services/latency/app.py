"""
The Flask application that realizes the service 'Latency'.
"""


from sys import path as pythonpath
from os.path import join, dirname, realpath
pythonpath.append(join(dirname(realpath(__file__)), "../../"))

from common.model.environment.webapp import WebApp as App
from services.latency.config import Debug as AppConfig
from services.latency.api.task import Task
from sys import argv


# Initialization
app = App(__name__, AppConfig)

# REST API
app.add_rest_api(Task, "/task")

# Shutdown
app.add_shutdown_hook(lambda: print("Goodbye!"))


if __name__ == "__main__":
    if len(argv) > 1:
        app.config["APP_PORT"] = int(argv[1])
    app.start(port=app.config["APP_PORT"])