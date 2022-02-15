"""
Fetch current lightcurve from Flows API.
"""

import os.path
import tempfile
from astropy.table import Table
from tendrils.api import get_api_token, get_request, URLS
from typing import Union


def get_lightcurve(target: Union[int, str]) -> Table:
    """
    Retrieve lightcurve from Flows server.

    Parameters:
        target (int): Target to download lightcurve for.

    Returns:
        :class:`astropy.table.Table`: Table containing lightcurve.

    TODO:
        - Enable caching of files.
    """
    token = get_api_token()
    # Send query to the Flows API:
    params = {'target': target}
    r = get_request(URLS.lightcurves_url, token=token, params=params)

    # Create temp directory and save the file into there,
    # then open the file as a Table:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpfile = os.path.join(tmpdir, 'table.ecsv')
        with open(tmpfile, 'w') as fid:
            fid.write(r.text)

        tab = Table.read(tmpfile, format='ascii.ecsv')

    return tab
