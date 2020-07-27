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

#jsonFileName = input("Enter the problem json file name: ")
#print(jsonFileName)
problemJSONFileName="problems.json"

#jsonFileName = input("Enter the cause json file name: ")
#print(jsonFileName)
causeJSONFileName="causes.json"

#jsonFileName = input("Enter the action json file name: ")
#print(jsonFileName)
actionJSONFileName="actions.json"


#jsonFileName = input("Enter the destination json file name: ")
#print(jsonFileName)
jsonFileName="failure_nesting.json"

with open(filepath + "\\" + categoryJSONFileName) as category_file:
    category_file_dict = json.load(category_file)
with open(filepath + "\\" + sourceJSONFileName) as source_file:
    source_file_dict = json.load(source_file)
with open(filepath + "\\" + problemJSONFileName) as problem_file:
    problem_file_dict = json.load(problem_file)
with open(filepath + "\\" + causeJSONFileName) as cause_file:
    cause_file_dict = json.load(cause_file)


#new failure code nesting dictionary
failure_code_dict = {}

#category, source, problem, cause, action dictionaries
category_dict = {}
source_dict = {}
problem_dict = {}
cause_dict = {}
new_source_dict = {}

#get category list
category_list = []
source_list = []
problem_list = []
cause_list = []

#loop through categories in category list
for category in category_file_dict['category']:
    category_name = category_dict['name'] = category['name']
    #loops through sources
    category_source = category['source']
    for source in category_source:
        source_dict = [i for i in source_file_dict['source'] if i['name']==source]
        if (len(source_dict)>0):
            new_source_dict['name'] = source_dict[0]['name']
            if ('problem' in source_dict[0].keys()):
                for problem in source_dict[0]['problem']:
                    problem_dict = [i for i in problem_file_dict if i['code']==problem]
                    if (len(problem_dict)>0):
                        problem_list.append(problem_dict[0]);
                    else:
                        print(problem + "NOT FOUND!")
            else:
                print(source + "HAS NO PROBLEMS!")
            if ('cause' in source_dict[0].keys()):
                for cause in source_dict[0]['cause']:
                    cause_dict = [i for i in cause_file_dict if i['code']==cause]
                    if (len(cause_dict)>0):
                        cause_list.append(cause_dict[0]);
                    else:
                        print(cause + "NOT FOUND!")
            else:
                print(source + "HAS NO PROBLEMS!")
            new_source_dict['problem']=problem_list
            new_source_dict['cause']=cause_list
            problem_list = []
            cause_list = []
            problem_dict = {}
            cause_dict = {}
            
            source_list.append(new_source_dict)
            new_source_dict = {}
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



