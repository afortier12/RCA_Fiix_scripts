import csv
import json

#filepath = input("Enter the file path for the Category/Source CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'

#csvFileName = input("Enter the csv file name: ")
#print(csvFileName)
csvFileName="[ITM-Windsor]ProblemCodes.csv"

#jsonFileName = input("Enter the json file name: ")
#print(jsonFileName)
jsonFileName="problems.json"

main_list = []
problem_dict = {}
with open(filepath + "\\" + csvFileName, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        #get data from csv row
        problem_dict['id'] = rows['id']
        problem_dict['code'] = rows['code']
        problem_dict['description'] = rows['description']
        main_list.append(problem_dict)  
        problem_dict={}

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(main_list, indent=4))
