from importlib.metadata import version

from .stylesheets import StyleDict, TufteStyleSheet  # noqa

__version__: str = version(__package__)
