"""Logging"""
from colorama import Fore

debug_on: bool = False


def debug(*args, **kwargs) -> None:
    """Log debug message"""
    if debug_on:
        print(*args, **kwargs)


def green(text: str) -> str:
    """Return green string"""
    return Fore.GREEN + text + Fore.RESET


def yellow(text: str) -> str:
    """Return yellow string"""
    return Fore.YELLOW + text + Fore.RESET
