import csv
import json

#filepath = input("Enter the file path for the Category/Source CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'

#csvFileName = input("Enter the csv file name: ")
#print(csvFileName)
csvFileName="Asset_category_source.csv"

#jsonFileName = input("Enter the json file name: ")
#print(jsonFileName)
jsonFileName="asset_category_tree.json"

main_dict = {}
category_dict = {}
category_data = []
source_data = []
last_id=''
with open(filepath + "\\" + csvFileName, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        #get data from csv row
        id = rows['Category']
        source = rows['Source']
        #first pass for category dictionary 
        if (len(category_dict)==0):
            category_dict['name'] = id
            if (len(source)>0):
                source_data.append(source)
        elif (last_id == id):
            if (len(source)>0):
                source_data.append(source)
        else:
            #add source list to category dictionary if not empty
            if (len(source_data)>0):
                category_dict['source']=(source_data)
            #add category dictionary to category list
            category_data.append(category_dict)
            #clear data from last id
            source_data = []
            category_dict = {}
            #create new source from current row
            category_dict['name'] = id
            if (len(source)>0):
                source_data.append(source)
        last_id = id
    
    #add last row to category list
    #add source list to category dictionary if not empty
    if (len(source_data)>0):
        category_dict['source']=(source_data)
    #add category dictionary to source list
    category_data.append(category_dict)
    main_dict['category']=category_data        

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(main_dict, indent=4))
