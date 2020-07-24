import csv
import json

#filepath = input("Enter the file path for the Source/Problem/Cause CSV file: ")
#print(filepath)
filepath = 'C:\\Users\\afortier.INTEGRITYPD\\Documents\Fiix'

#csvFileName = input("Enter the csv file name: ")
#print(csvFileName)
csvFileName="Asset_problem_tree.csv"

#jsonFileName = input("Enter the json file name: ")
#print(jsonFileName)
jsonFileName="asset_tree.json"

main_dict = {}
source_dict = {}
source_data = []
problem_data = []
cause_data = []
last_id=''
with open(filepath + "\\" + csvFileName, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        #get data from csv row
        id = rows['Source']
        problem = rows['Problem']
        cause = rows['Cause']
        if (len(problem)>0):
            problem_data.append(problem)
        if (len(cause)>0):
            cause_data.append(cause)
        #first pass for source dictionary 
        if (len(source_dict)==0):
            source_dict['name'] = id
        elif (last_id != id):
            #add problem and cause lists to source dictionary if not empty
            if (len(problem_data)>0):
                source_dict['problem']=(problem_data)
            if (len(cause_data)>0):
                source_dict['cause']=cause_data
            #add source dictionary to source list
            source_data.append(source_dict)
            #clear data from last id
            problem_data = []
            cause_data = []
            source_dict = {}
            #create new source from current row
            if (len(problem)>0):
                problem_data.append(problem)
            if (len(cause)>0):
                cause_data.append(cause)
            source_dict['name'] = id
        last_id = id
    
    #add last row to source list
    #add problem and cause lists to source dictionary if not empty
    if (len(problem_data)>0):
        source_dict['problem']=(problem_data)
    if (len(cause_data)>0):
        source_dict['cause']=cause_data
    #add source dictionary to source list
    source_data.append(source_dict)
    main_dict['source']=source_data        

with open(filepath + "\\" + jsonFileName, 'w') as jsonFile:
    jsonFile.write(json.dumps(main_dict, indent=4))
