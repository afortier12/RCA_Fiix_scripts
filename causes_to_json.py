import csv
import json

#filepath = input("Enter the file path for the Category/Source CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'

#csvFileName = input("Enter the csv file name: ")
#print(csvFileName)
csvFileName="[ITM-Windsor]CauseCodes.csv"

#jsonFileName = input("Enter the json file name: ")
#print(jsonFileName)
jsonFileName="causes.json"

main_list = []
cause_dict = {}
with open(filepath + "\\" + csvFileName, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        #get data from csv row
        cause_dict['id'] = rows['id']
        cause_dict['code'] = rows['code']
        cause_dict['description'] = rows['description']
        main_list.append(cause_dict)  
        cause_dict={}

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(main_list, indent=4))
