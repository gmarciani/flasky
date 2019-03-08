"""
Configurations for the service 'Latency'.
"""


class Default:
    """
    Default configuration.
    """
    DEBUG = True

    LOG_LEVEL = "INFO"

    APP_HOST = "localhost"
    APP_PORT = 18001


class Debug(Default):
    """
    Debug configuration.
    """
    DEBUG = True

    LOG_LEVEL = "DEBUG"


class Production(Default):
    """
    Production configuration.
    """
    DEBUG = False