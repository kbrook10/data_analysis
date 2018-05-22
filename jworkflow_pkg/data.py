# Step 19: Import necessary libraries and clean up notebook flow
import os
from urllib.request import urlretrieve
import pandas as pd

# Step 1: Save URL for bike data

BIKE_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# Step 18: Only download data if it does not already exist
def get_bdata(filename='fremont.csv', url=BIKE_URL, 
    force_download=False):
    """
    Download and cache the bike data
    
    Parameters:
    ----------
    filename : string (optional)
        location to same the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force re-download of data

    Returns:
    --------
    data : pandas.DataFrame
        The bike data

    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL,'fremont.csv')
    bdata = pd.read_csv('fremont.csv', index_col='Date')
    try:
        bdata.index = pd.to_datetime(bdata.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        bdata.index = pd.to_datetime(bdata.index)

    bdata.columns = ['West', 'East']
    bdata['Total'] = bdata['West'] + bdata['East']
    return bdata
