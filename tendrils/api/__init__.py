"""
API subpackage. Also contains base functions.
"""
# flake8: noqa

from .catalogs import get_catalog, get_catalog_missing
from .datafiles import get_datafile, get_datafiles
from .filters import get_filters
from .lightcurves import get_lightcurve
from .photometry_api import get_photometry, upload_photometry
from .set_photometry_status import set_photometry_status, cleanup_photometry_status
from .sites import get_site, get_all_sites
from .targets import get_targets, get_target, add_target
from ..utils import load_config, urls
from typing import Optional
from warnings import warn
import requests

URLS = urls()


def get_api_token() -> str:
    """
    Get api token from config file or raise.
    Returns: str = token as a string

    """
    # Get API token from config file:
    config = load_config()
    token = config.get('api', 'token', fallback=None)
    if token is None:
        raise RuntimeError("No API token has been defined")

    return token


def get_request(url: str, token: str = None, params: Optional[dict] = None,
                headers: Optional[dict] = None) -> requests.Response:
    """
    Make a get request using request with given url, params, and header. Token can be given inplace of header
    to create a default header that uses the token.
    Args:
        url: str = url for get request
        token: Optional[str] = api token. Can also be provided as part of headers dict.
        params: Optional[dict] = dict of params
        headers: Optional[dict] = headers dict. Can also be created from just the token.

    Returns: requests.Response

    """
    params = {} if params is None else params
    headers = {} if headers is None else headers
    if not headers and token is None:
        warn('headers and token was None but one should probably give the authorization token')
    elif token is not None:
        headers['Authorization'] = 'Bearer ' + token

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response


def post_request(url: str, token: str = None, params: Optional[dict] = None, data: Optional[dict] = None,
                 headers: Optional[dict] = None, files: Optional[dict] = None) -> requests.Response:
    """
    Make a post request using request with given url, params, and header. Token can be given inplace of header
    to create a default header that uses the token.
    Args:
        url: str = url for get request
        token: str, optional = api token. Can also be provided as part of headers dict.
        params: dict, optional = dict of params
        data: dict, optional = dict of data
        headers: dict, optional = headers dict. Can also be created from just the token.
        files: dict, optional = files dict.

    Returns: requests.Response
    """
    data = {} if data is None else data
    params = {} if params is None else params
    files = {} if files is None else files
    headers = {} if headers is None else headers
    if not headers and token is None:
        warn('headers and token was None but one should probably give the authorization token')
    elif token is not None:
        headers['Authorization'] = 'Bearer ' + token

    response = requests.post(url, data=data, params=params, files=files, headers=headers)
    response.raise_for_status()
    return response
