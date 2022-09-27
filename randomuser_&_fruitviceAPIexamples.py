"""
    Random User and Fruitvice API Examples

Author: Ana M. Almeida
Date: 27.09.2022

Guide: https://github.com/anamvalmeida/courses/blob/Applied-AI/API_examples_v2.ipynb
"""

from randomuser import RandomUser
import pandas as pd

# CREATE RANDOM USER API
print('CREATE RANDOM USER API')
print(' ')

# Create random user object
r = RandomUser()

# Get a list of random 10 users
some_list = r.generate_users(10)
print('List of 10 random users:',some_list)
print(' ')

# From the 'Get Methods', it can be generate the required
# parameters to construct a dataset. For example:
name = r.get_full_name()
print('List of 10 random users (full name and email):')
for user in some_list:
    print(user.get_full_name()," ",user.get_email())

# Generate five photos
for user in some_list:
    print(user.get_picture())
print(' ')

# Generate a table with information about the users
def get_users():
    users = []

    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender,
                      "City":user.get_city,"State":user.get_state(),
                      "Email":user.get_email(),"DOB":user.get_dob(),
                      "Picture":user.get_picture()})
    return pd.DataFrame(users)

print('Data Frame:')
df1 = pd.DataFrame(get_users()) # Returns the table organized.
print(df1) # Returns the size of the array.
print(' ')

# FRUITVICE API
print('FRUITVICE API')
print(' ')

import requests
import json

data = requests.get('https://www.fruityvice.com/api/fruit/all')
print('Data:',data)

results = json.loads(data.text)
print('Result of JSON:',results)

print('Data Frame:')
pd.set_option('display.max_columns', None) # To see the complete table. Otherwise, it will be shorted.
print(pd.DataFrame(results)) # The result is in a nested json format. The 'nutrition'
# column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
print(' ')

df2 = pd.json_normalize(results)
print('New Data Frame:')
print(df2)

# Extract information from the dataframe
cherry = df2.loc[df2["name"] == "Cherry"]
print('Cherry Information')
print('Location Result:',cherry)
print('Family:',cherry.iloc[0]['family'])
print('Genus:',cherry.iloc[0]['genus'])

banana = df2.loc[df2["name"] == "Banana"]
print('Banana Information')
print('Calories:',banana.iloc[0]['nutritions.calories'])
print(' ')

# Extract information from APIs
data_api = requests.get('https://www.fishwatch.gov/api/species')
print('Data API:',data_api)

results_api = json.loads(data_api.text)
print(pd.DataFrame(results_api))
