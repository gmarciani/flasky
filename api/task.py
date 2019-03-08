"""
The REST API that simulates tasks through random latency.
"""


from flask_restful import Resource
from random import uniform
from time import sleep


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
        task_latency = uniform(1, 5)
        sleep(task_latency)
        return dict(status="OK", task_latency=task_latency)