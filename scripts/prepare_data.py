import requests
import hashlib
import zipfile
import pandas as pd

url = 'https://archive.ics.uci.edu/static/public/19/car+evaluation.zip'
response = requests.get(url)

expected_hash_c45 = 'cc75bb7e71f94a6436a3d2b72575c5917b08b18f6792395a6045770086a3e8fb'
expected_hash_car_data = 'b703a9ac69f11e64ce8c223c0a40de4d2e9d769f7fb20be5f8f2e8a619893d83'
expected_hash_car_names = '9835ccf47cdbd111577adc50000d6d247f71a31fd6ef84bf25181449685d22bd'

response = requests.get(url)

with zipfile.ZipFile('car+evaluation.zip',mode = 'r') as archive:
    archive.extractall(path='data')

c45 = 'data/car+evaluation/car.c45-names'
data = 'data/car+evaluation/car.data'
names = 'data/car+evaluation/car.names'

def hash_compare(filename, hash_value):
    try:
        with open(filename, mode='rb') as file:
            data = file.read()
            sha256hash = hashlib.sha256(data).hexdigest()
            return sha256hash == hash_value
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False

result1 = hash_compare(c45, expected_hash_c45)
result2 = hash_compare(data, expected_hash_car_data)
result3 = hash_compare(names, expected_hash_car_names)
print("c45 hash match:", result1)
print("data hash match:", result2)
print("names hash match:", result3)


file_path = 'data/car.data'
df = pd.read_csv(file_path, delimiter=',', header=None)
output_path = 'data/cardata.csv'
column_headers = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'condition']

# Assign the column names to the DataFrame
df.columns = column_headers
df.to_csv(output_path, index=False)
