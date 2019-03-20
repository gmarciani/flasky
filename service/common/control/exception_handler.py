from flask import jsonify
from datetime import datetime
from service.common.model.exceptions.rest_exceptions import RESTException


def handle_exception(exc):
    """
    Handle all exceptions.
    :param exc: (Exception) the exception.
    :return: (code, response)
    """
    response = jsonify({
        "ts": datetime.now(),
        "error": str(exc)
    })
    return response, exc.code if isinstance(exc, RESTException) else 500