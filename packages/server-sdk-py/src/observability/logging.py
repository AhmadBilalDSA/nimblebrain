// Modified: changed logger.error to logger.warning for caller-side errors

from __future__ import annotations

import logging
import sys
from collections.abc import MutableMapping
from typing import Any

import structlog
from opentelemetry import trace

fro