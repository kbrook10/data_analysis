### Step 1: Unit Testing Import necessary libraries
import pandas as pd
import numpy as np
from urllib.request import urlretrieve

### Step 2: Import package to test                                            
from jworkflow_pkg.data import get_bdata

# Step 6: Place assertions into a function
def test_bike_data():
    data = get_bdata()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time)) == 24
