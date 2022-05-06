import json
import csv
from datetime import date, datetime, timedelta
from xml.etree import ElementTree as et

def modify_xml(x,y):
    today = date.today()
    departdate = datetime.today() + timedelta(days=x)
    returndate = datetime.today() + timedelta(days=y)
    tree = et.parse('test_payload1.xml')
    tree.find('.//DEPART').text = str(departdate)
    tree.find('.//RETURN').text = str(returndate)
    tree.write('test_payload_result.xml')

def modify_json(x):
    filename = 'test_payload.json'
    resultfilename = 'test_payload_result.json'
    with open(filename, 'r+') as file:
     resultjsonfile = open(resultfilename, 'w')
    # First we load existing data into a dict.
     file_data = json.load(file)
     new_file_data = file_data
     if x in file_data.keys():
        del new_file_data[x]
    json.dump(new_file_data, resultjsonfile, indent = 4)
    file.close()
    resultjsonfile.close()

def modify_csv():
    filename1 = 'Jmeter_log1.jtl'
    filename2 = 'Jmeter_log2.jtl'
    with open(filename1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] != 200:
                print(row[2]+"--"+row[3]+"--"+row[4]+"--"+row[8]+"--"+row[1])

if ( __name__ == "__main__"):
    modify_xml(1,1)
    modify_json('outParams')
    modify_csv()