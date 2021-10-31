# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
listingsBarcelona_prepared = dataiku.Dataset("listingsBarcelona_prepared")
listingsBarcelona_prepared_df = listingsBarcelona_prepared.get_dataframe()


# Compute recipe outputs from inputs

maxlat = barcelona_Polygon_df['latitude'].max()
maxlon = barcelona_Polygon_df['longitude'].max()
minlat = barcelona_Polygon_df['latitude'].min()
minlon = barcelona_Polygon_df['longitude'].min()


# Write recipe outputs
barcelona_Polygon = dataiku.Dataset("Barcelona_Polygon")
barcelona_Polygon.write_with_schema(barcelona_Polygon_df)
