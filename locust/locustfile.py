from locust import HttpLocust, TaskSet, task
import random


class FlaskyTasks(TaskSet):

    @task(1)
    def simple(self):
        self.client.get("/task")

    @task(2)
    def random_latency(self):
        self.client.get("/task?latencyMin=1&latencyMax=10")

    @task(3)
    def random_io(self):
        self.client.get("/task?fileMin=1000000&fileMax=10000000")


class FlaskyLocustUniform(HttpLocust):
    weight = 1
    task_set = FlaskyTasks
    wait_function = lambda self: random.uniform(5000, 9000)