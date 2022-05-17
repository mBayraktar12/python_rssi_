import json
import os
import glob
import pandas as pd



def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,"*json"))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files

beacon_data = get_files("json_datas")

filepath = beacon_data[0]

df = pd.read_json(filepath, lines = True)
print(df.head())

data_list = []

for data in beacon_data:
    with open(data) as doc:
        exp = json.load(doc)
        data_list.append(exp)

print(data_list[:2])


