#PYTHON SCRIPT FOR ONE-HOT ENCODING

import numpy as np
import pandas as pd

data = pd.read_csv(input("Enter path to database/dataset file (.csv): ")) #Dataset initially containing NULL values and categorical data
print(data.head(50)) #Print first 50 rows for observing the differences before and after running the operations

categorical_data=data.select_dtypes(include=['object']).columns.tolist() #Saves the columns with categorical data into a python list

one_hot=['Item_Type','Outlet_Type'] #List of columns to apply One Hot encoding on

print(f"Col: Outlet_Type has {data['Outlet_Type'].nunique()} unique entries")
print(f"Col: Item_Type has {data['Item_Type'].nunique()} unique entries")

n_unique_outlet_type=data['Outlet_Type'].nunique()
n_unique_item_type=data['Item_Type'].nunique()
max_for_one_hot=30 #Reference bound: For example, if we have more than 30 unique entries (cardinality) in the feature column, then do not do One-Hot Encoding

if n_unique_outlet_type<max_for_one_hot:
    outlet_type=data['Outlet_Type'].unique()
    for i in outlet_type:
        column_name = f'Outlet_Type_{i.replace(" ", "_")}'
        data[column_name] = (data['Outlet_Type'] == i).astype(int)
    data = data.drop('Outlet_Type', axis=1)
else:
    print("Cannot do One-Hot encoding.. Cardinality is too high")
if n_unique_item_type<max_for_one_hot:
    item_type=data['Item_Type'].unique()
    for i in item_type:
        column_name = f'Item_Type_{i.replace(" ", "_")}'
        data[column_name] = (data['Item_Type'] == i).astype(int)
    data = data.drop('Item_Type', axis=1)
else:
    print("Cannot do One-Hot encoding.. Cardinality is too high")

data.to_csv(input("\n\nEnter path to save file: "), index=False) #Save the data after One-Hot encoding
print("\n\n\nOne-Hot Encoding successful")