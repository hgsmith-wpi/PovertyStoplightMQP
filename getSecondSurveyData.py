import pandas as pd
import os
import glob

#get all excel files under the path
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

firstSurveys = []
secondSurveys = []

#add up how many second surveys each organization has
def countSecondSurveys(df):
    #get Survey Number and Organization 
    organizationDict = {}
    organizations = df['Organization']
    families = df['Family code']
    surveys = df['Survey number']
    for i in range(len(surveys)):
        if surveys[i] == "1º":
            firstSurveys.append(families[i])
        elif surveys[i] == "2º":
            secondSurveys.append(families[i])
        if families[i] in firstSurveys and families[i] in secondSurveys:
            if organizations[i] in organizationDict:
                organizationDict[organizations[i]] = organizationDict.get(organizations[i]) + 1
            else:
                organizationDict[organizations[i]] = 1
    return organizationDict

#print out the organizations with their amount of follow-up surveys
for file in csv_files:
    df = pd.read_excel(file)
    print(file)
    organizationDict = countSecondSurveys(df)
    keys = organizationDict.keys()
    for key in keys:
        print(key + ": " + str(organizationDict.get(key)))

