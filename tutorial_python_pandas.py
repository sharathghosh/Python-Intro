# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:26:46 2016

@author: sharath
"""

import pandas as pd



# Reading csv files
data = pd.read_csv('train.csv', encoding='utf-8')
# Using an already available column as index
data = pd.read_csv('train.csv', encoding='utf-8', index_col='Id')



# Select a column, group of columns
data_city = data['City']
data_city_group = data['City Group']
data_city_and_group = data[['City', 'City Group', 'revenue']]



# Select a set of rows
idx = data_city_and_group['City'] == 'Ankara'
data_ankara = data_city_and_group[idx]
idx = data_city_and_group['City'] == 'Bursa'
data_bursa = data_city_and_group[idx]



# Append dataframes
data_ankara_bursa = data_ankara.append(data_bursa)



# Aggregation
# Get count of number of items for Ankara
z = pd.groupby(data_ankara_bursa, ['City']).agg(['count'])
z.loc['Ankara']['City Group']['count']
z.loc['Bursa']['City Group']['count']


# Get mean revenue for Bursa
z = pd.groupby(data_ankara_bursa, ['City']).agg(['mean'])
z.loc['Bursa']['revenue']['mean']

# Check with mean computed from dataframe
data_bursa['revenue'].mean() == z.loc['Bursa']['revenue']['mean']



# Operations on columns
data_ankara['revenue'].min()
data_ankara['revenue'].max()

# Adding columns
import numpy as np
import copy
temp = copy.deepcopy(data_ankara)
temp['revenue_log10'] = np.log10(data_ankara['revenue'])

# Adding and initializing a column
temp['my_column'] = 0.0

# Remove columns and dataframes
del temp['revenue_log10']
del temp['my_column']
del temp

# Unique items in a column
unique = data['City'].unique()



# Create dataframes from scratch
my_df = pd.DataFrame(columns=['country', 'city', 'wish_list'])

# Adding data one item at a time
my_df.loc[0] = ['India', 'New Delhi', 'Y']
my_df.loc[1] = ['Italy', 'Rome', 'Y']
my_df.loc[2] = ['USA', 'Washington D.C.', 'N']
my_df.loc[3] = ['Russia', 'Moscow', 'N']
my_df.loc[4] = ['Egypt', 'Cairo', 'N']
my_df.loc[5] = ['Greece', 'Athens', 'Y']

# Adding data using a dictionary
country_data = {'country': ['India', 'Italy', 'USA', 'Russia', 'Egypt', 'Germany', 'Hungary'],
                'city' : ['New Delhi', 'Rome', 'Washington D.C.', 'Moscow', 'Cairo', 'Berlin', 'Budapest'],
                'wish_list': ['Y', 'Y', 'N', 'N', 'N', 'Y', 'N']}

my_new_df = pd.DataFrame(columns=['country', 'city', 'wish_list'], data=country_data)



# Joining dataframes
# inner join
pd.merge(my_df, my_new_df, on=['country'], how='inner')
# outer join
pd.merge(my_df, my_new_df, on=['country'], how='outer')
# left outer join
pd.merge(my_df, my_new_df, on=['country'], how='left')
# right outer join
pd.merge(my_df, my_new_df, on=['country'], how='right')



# Iterating over items in a dataframe
for item in data['City']:
    print item

for index, row in data.iterrows():
    print row['City'], row['revenue']



# Saving dataframes
data_city_and_group.to_csv('data_city_and_group.csv', encoding='utf-8')


