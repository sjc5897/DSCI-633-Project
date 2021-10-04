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
Simply prints the shape of the file, meaning the number of rows (entities) and columns (attributes)

@input:     df  -   dataframe, the dataframe that you wish to be described
@output:    void
"""
def print_shape(df):
    row, columns = df.shape
    print("Data Shape (Row Count and Column Count):\n \trows: " + str(row) + " column: " + str(columns))


"""
Prints out the column information, currently the value counts of each column

@input      df  -   dataframe, the dataframe that you wish to be described
@output     void
"""
def print_column_information(df):
    print("Column Information:")
    column_array = df.columns
    for column_name in column_array:
        print(str(df[column_name].value_counts()))


"""
Main function, loads in the file into pandas
"""
if __name__ == '__main__':
    filename = "mental_health_data.csv"  # our data file

    # read the csv, df (dataframe) is type pandas.dataframe
    df = pd.read_csv('mental_health_data.csv')

    # print the df (dataframes)
    print_shape(df)

    # print column data
    print_column_information(df)
