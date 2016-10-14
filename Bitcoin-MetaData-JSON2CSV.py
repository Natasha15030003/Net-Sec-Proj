import json
import pdb
import csv
from pprint import pprint

#### Variables Used in the Code
INPUT_FILE_NAME = 'merge_COMPLETE.json'
OUTPUT_FILE_NAME = 'my_file.csv'
data2 =[]

#### Load Json Data
with open(INPUT_FILE_NAME) as data_file:    
    data = json.load(data_file)

#### Extract Data for CSV file
for d in range(len(data)):
    if (len(data[d]['labels']) > 0):
        for i in range(len(data[d]['labels'])):
            data2.append({'labels':str(data[d]['labels'][i]['name']), 'user':data[d]['user']['login'], 'user_id':data[d]['user']['id'], 'created_at':data[d]['created_at'], 'closed_at':data[d]['closed_at']})

#### Open Output file and write data to CSV file
with open(OUTPUT_FILE_NAME, 'w') as f:
	for d in xrange(len(data2)):
                f.write("\n")
                print d
		for key in data2[d].keys():
		   print key
		   f.write( str(data2[d][key]) + ",");
