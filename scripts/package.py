# You probably don't want to run this again as is, it was just used to get a datapackage.json stub setup.

import datapackage
import io
import csv
from jsontableschema import infer

dp = datapackage.DataPackage()
dp.descriptor['name'] = 'australian-political-donations'
dp.descriptor['title'] = 'Australian political donations'

filepath = './data/donor-declarations-categorised-2016.csv'

with io.open(filepath) as stream:
    headers = stream.readline().rstrip('\n').split(',')
    values = csv.reader(stream)
    schema = infer(headers, values)
    dp.descriptor['resources'] = [
        {
            'name': 'donor-declarations-categorised-2016',
            'path': filepath,
            'schema': schema
        }
    ]

with open('datapackage.json', 'w') as f:
    f.write(dp.to_json())