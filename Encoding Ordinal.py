#PYTHON SCRIPT FOR ORDINAL ENCODING

import numpy as np
import pandas as pd

data = pd.read_csv(input("Enter path to database/dataset file (.csv): ")) #Dataset initially containing NULL values and categorical data
print(data.head(50)) #Print first 50 rows for observing the differences before and after running the operations

categorical_data=data.select_dtypes(include=['object']).columns.tolist() #Saves the columns with categorical data into a python list

ordinal=['Item_Fat_Content','Outlet_Size','Outlet_Locaion_Type'] #List of columns to apply Ordinal encoding on

'''print(f"Col Item_Fat_Content: {data['Item_Fat_Content'].unique()}")
print(f"Col Outlet_Size: {data['Outlet_Size'].unique()}")
print(f"Col Outlet_Location_Type: {data['Outlet_Location_Type'].unique()}")
print(f"Col Outlet_Type: {data['Outlet_Type'].unique()}")
print(f"Col Item_Type: {data['Item_Type'].unique()}")


fat_content_map = {'LF': 'Low Fat', 'low fat': 'Low Fat', 'reg': 'Regular'}
data['Item_Fat_Content'] = data['Item_Fat_Content'].replace(fat_content_map)

data['Outlet_Size'] = data['Outlet_Size'].fillna('Unknown')''' #For normalizing values to make them ready for Encoding

map_fat = {'Low Fat': 0, 'Regular': 1}
map_size = {'Small': 1, 'Medium': 2, 'High': 3, 'Unknown': 0}
map_loc_type = {'Tier 1': 2, 'Tier 2': 1, 'Tier 3': 0}

data['Item_Fat_Content'] = data['Item_Fat_Content'].replace(map_fat)
data['Outlet_Size'] = data['Outlet_Size'].replace(map_size)
data['Outlet_Location_Type'] = data['Outlet_Location_Type'].replace(map_loc_type)

print(data.head(50))

data.to_csv(input("\n\nEnter path to save file: "), index=False) #Save the data after ordinal encoding
print("\n\n\nOrdinal Encoding successful")