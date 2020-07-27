import csv
import json

#filepath = input("Enter the file path for the Category/Source CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'


#jsonFileName = input("Enter the category json file name: ")
#print(jsonFileName)
categoryJSONFileName="asset_category_tree.json"

#jsonFileName = input("Enter the asset json file name: ")
#print(jsonFileName)
sourceJSONFileName="asset_tree.json"

#jsonFileName = input("Enter the destination json file name: ")
#print(jsonFileName)
jsonFileName="failure_nesting.json"

with open(filepath + "\\" + categoryJSONFileName) as category_file:
    category_file_dict = json.load(category_file)
with open(filepath + "\\" + sourceJSONFileName) as source_file:
    source_file_dict = json.load(source_file)

#new failure code nesting dictionary
failure_code_dict = {}

#category and source dictionaries
category_dict = {}
source_dict = {}

#get category list
category_list = []
source_list = []


#loop through categories in category list
for category in category_file_dict['category']:
    category_name = category_dict['name'] = category['name']
    #loops through sources
    category_source = category['source']
    for source in category_source:
        source_dict = [i for i in source_file_dict['source'] if i['name']==source]
        if (len(source_dict)>0):
            source_list.append(source_dict)
        else:    
            print(source + "NOT FOUND!")
        source_dict={}
    
    category_dict['source'] = source_list
    category_list.append(category_dict)
    category_dict = {}
    source_dict={}
    source_list = []

#add category dictionary to source list
failure_code_dict['category']=category_list  

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(failure_code_dict, indent=4))

