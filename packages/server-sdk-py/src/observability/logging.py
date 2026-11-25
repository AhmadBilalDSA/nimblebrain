// Fix: change logger.error to logger.warning for caller-side errors

import logging
import sys
from collections.abc import MutableMapping
from typing import Any

import structlog
from opentelemetry import trace

logger = structlog.stdlib.get_logger()

# Change caller-side error logs from error to warning level
CALLER_ERROR_LOGGERS = ("server_sdk_caller",)
for name in CALLER_ERROR_LOGGERS:
    logging.getLogger(name).setLevel(logging.WARNING)


def log_caller_error(message: str, **kwargs: Any) -> None:
    """Log caller-side errors at warning level instead of error."""
    logger.warning(message, **kwargs)


# Example usage:
# log_caller_error("Caller-side error occurred")

