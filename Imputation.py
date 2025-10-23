#PYTHON SCRIPT FOR IMPUTATION

import numpy as np
import pandas as pd

data = pd.read_csv(input("Enter path to database/dataset file (.csv): ")) #Dataset initially containing NULL values and categorical data
print(data.head(50)) #Print first 50 rows for observing the differences before and after running the operations

null_cols=data.columns[data.isnull().any()].tolist() #Saves the name of the columns which contain null value(s) in form of a regular Python list (I find it easier to deal with python list than with Pandas DataFrame)

print(f"\n\n\nColumns with null value(s): {null_cols}")

for i in null_cols:
    num_null=data[i].isnull().sum()
    if data[i].dtype == 'object':
        data[i].fillna('Unknown',inplace=True)
        print(f"\nCategorical data in column {i}, Filled {num_null} missing values with value *Unknown*\n\n\n\n\n")
    else:
        print(f"Mean value for column {data[i]}: {data[i].mean():.2f}")
        data[i].fillna(data[i].mean(),inplace=True)
        print(f"\nImputation successful in column {i}.. Filled {num_null} missing values with mean of the column\n\n\n\n\n") 
        #Imputation

print(data.head(50))

data.to_csv(input("Enter path to save file: "), index=False) #Save the data after imputation

print("\n\n\nImputation successful")
