import json
import pandas as pd
import csv

# Read the data from file
# We now have a Python dictionary
with open('data.json',encoding='UTF-8') as f:
    data_listofdict = json.load(f)

# Writing a list of dicts to CSV
keys = data_listofdict[0].keys()
with open('saved_data.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data_listofdict)
