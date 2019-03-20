class SimpleSchedulerJob:
    """
    A job for the scheduler.
    """

    def __init__(self, name, func, trigger, kwargs=None):
        """
        Creates a new job for the scheduler.
        :param name: the job name.
        :param func: the function to execute.
        :param trigger: the function trigger.
        :param kwargs: the arguments for the function.
        """
        self.name = name
        self.func= func
        self.kwargs = kwargs
        self.trigger = trigger