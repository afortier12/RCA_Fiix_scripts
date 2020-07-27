import csv
import json

#filepath = input("Enter the file path for the Category/Source CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'

#csvFileName = input("Enter the csv file name: ")
#print(csvFileName)
csvFileName="[ITM-Windsor]ActionCodes.csv"

#jsonFileName = input("Enter the json file name: ")
#print(jsonFileName)
jsonFileName="actions.json"

main_list = []
action_dict = {}
with open(filepath + "\\" + csvFileName, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        #get data from csv row
        action_dict['id'] = rows['id']
        action_dict['code'] = rows['code']
        action_dict['description'] = rows['description']
        main_list.append(action_dict)  
        action_dict={}

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(main_list, indent=4))
