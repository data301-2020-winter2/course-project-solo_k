# does this need to be here? 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(path)
          .drop_duplicates(subset=['latitude', 'longitude'])
          .dropna()
        .reset_index() 
          
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(...)
      )

    # Make sure to return the latest dataframe

    return cleaned_data

NA_val = df.isna().sum() 

