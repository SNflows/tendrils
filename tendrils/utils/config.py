"""
Functions for dealing with configuration of Tendrils API using .ini files or secrets.
"""

import configparser
import os.path
from functools import lru_cache


@lru_cache(maxsize=1)
def load_config(filename: str = 'config.ini') -> configparser.ConfigParser:
    """
    Load configuration file. Defaults to searching for config.ini but a custom name can be given.

    Returns:
        ``configparser.ConfigParser``: Configuration file.

    .. codeauthor:: Rasmus Handberg <rasmush@phys.au.dk>
    .. codeauthor:: Emir Karamehmetoglu <emir.k@phys.au.dk>
    """

    config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"{filename} file not found")

    config = configparser.ConfigParser()
    config.read(config_file)
    return config
