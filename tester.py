import pandas as pd
import numpy as np

if __name__ == '__main__':
    mental_health_data_filename = 'mental_health_data_true.csv'
    mental_health_df = pd.read_csv(mental_health_data_filename)

    mental_health_df["EEE"] = mental_health_df["EEE"].replace(regex=r'(?i)(female|woman|f)', value="F")

    print(mental_health_df["EEE"].unique())
