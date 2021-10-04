"""
DSCI-633 Project, Data Exploration Phase

This is a python script using pandas that will help us explore some cool data

@author:    Stephen Cook <sjc5897@rit.edu>
@language:  Python 3
@created:   10/1/21
@last edit: 10/4/21
"""

# Imports
import pandas as pd
import numpy as np
# /Imports

"""
Main function, loads in the file into pandas
"""
if __name__ == '__main__':
    filename = "mental_health_data.csv"  # our data file

    # read the csv, df (dataframe) is type pandas.dataframe
    df = pd.read_csv('mental_health_data.csv')

    # print the df (dataframes)
    print(df.shape)
    print(df)

