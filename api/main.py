"""Development entry point: uvicorn api.main:app --no-access-log."""

import logging

from atlas.serving.app import app

logging.basicConfig(level=logging.INFO, format="%(message)s")
__all__ = ["app"]
