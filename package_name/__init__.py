import warnings
from . import config

CONFIG = config.ConfigManager()

from pkg_resources import get_distribution

__version__ = get_distribution("pythonpackage").version

# TODO: update Telescope "names" fields
# TODO: document custom Image using _get_data_header
