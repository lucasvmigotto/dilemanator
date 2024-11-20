from logging import basicConfig
from rich.logging import RichHandler

from utils.settings import Settings

def setup_log(settings: Settings) -> None:
    handlers: list = None

    if settings.MODE_DEBUG or settings.MODE_VERBOSE:
        handlers = [RichHandler()]

    log_format: str = (
        '%(message)s'
        if handlers is not None
        else settings.LOG_FORMAT
    )

    basicConfig(
        level=settings.LOG_LEVEL,
        datefmt=settings.LOG_DATE_FORMAT,
        format=log_format,
        handlers=handlers
    )
