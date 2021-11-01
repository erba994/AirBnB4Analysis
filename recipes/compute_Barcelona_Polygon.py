# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import re

# Read recipe inputs
listingsBarcelona_prepared = dataiku.Dataset("listingsBarcelona_prepared")
listingsBarcelona_prepared_df = listingsBarcelona_prepared.get_dataframe()


# Compute recipe outputs from inputs

maxlat = listingsBarcelona_prepared_df['latitude'].max()
maxlon = listingsBarcelona_prepared_df['longitude'].max()
minlat = listingsBarcelona_prepared_df['latitude'].min()
minlon = listingsBarcelona_prepared_df['longitude'].min()

lon = [maxlon, minlon]
lat = [maxlat, minlat]
coord = [(x,y) for x in lon for y in lat]

col1 = 'POLYGON '+ str([str(str(coord[x][0]) + ' ' + str(coord[x][1])) for x,v in enumerate(coord)])
col1 = re.sub('\[','((',col1)
col1 = re.sub('\[','((',col1)
col1 = re.sub('\]','))',col1)
col1 = re.sub('\'', '',col1)
print(col1)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
barcelona_Polygon_df = pd.DataFrame(col1, index =['1'], columns =['Polygon'])

# Write recipe outputs
barcelona_Polygon = dataiku.Dataset("Barcelona_Polygon")
barcelona_Polygon.write_with_schema(barcelona_Polygon_df)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# POLYGON ['2.2296735499641933 41.46306', '2.2296735499641933 41.352608000000004', '2.09159 41.46306', '2.09159 41.352608000000004']