from typing import Any

from bottle import route

@route("/")
def index() -> Any:
    """Player entry"""
    return "Hi player!"
