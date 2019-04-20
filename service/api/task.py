"""
The REST API that simulates tasks through random latency.
"""


from flask_restful import Resource
from flask import request
from random import uniform, randint
from time import sleep
import os
import socket
import uuid


class Task(Resource):
    """
    The Flask resource realizing the REST API that simulates tasks through random latency.
    """

    def get(self):
        """
        Get the status of the service.
        Returns
        -------
        res : dict
            The response.
        """
        latency_min = request.args.get("latencyMin")
        latency_max = request.args.get("latencyMax")
        file_min = request.args.get("fileMin")
        file_max = request.args.get("fileMax")

        task_latency = self.execute_latency(latency_min, latency_max)
        file_size = self.execute_io(file_min, file_max)

        host = socket.gethostname()
        return dict(status="OK", host=host, task_latency=task_latency, file_size=file_size, request=request.args)

    def execute_latency(self, min, max):
        task_latency = None
        if min is not None and max is not None and min <= max:
            task_latency = uniform(int(min), int(max))
            sleep(task_latency)
        return task_latency

    def execute_io(self, min, max):
        file_size = None
        if min is not None and max is not None and min <= max:
            filename = "flasky-{}".format(uuid.uuid1())
            file_size = randint(int(min), int(max))
            with open(filename, 'wb') as file:
                file.write(os.urandom(file_size))
            os.remove(filename)
        return file_size