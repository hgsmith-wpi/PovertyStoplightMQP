import pandas as pd
import os
import glob

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))

firstSurveys = []
secondSurveys = []

data = pd.DataFrame()

#get all follow-up surveys
def countSecondSurveys(df):
    #get Survey Number and Organization 
    families = df['familyCode']
    surveys = df['surveyNumber']
    firstAndSecondSurveys = []
    for i in range(len(surveys)):
        if surveys[i] == "1º":
            firstSurveys.append(families[i])
        elif surveys[i] == "2º":
            secondSurveys.append(families[i])
        if families[i] in firstSurveys and families[i] in secondSurveys:
            firstAndSecondSurveys.append(families[i])
    return firstAndSecondSurveys

#get families with follow-up surveys
for file in csv_files:
    df = pd.read_excel(file, sheet_name="Families")
    surveys = countSecondSurveys(df)
    for survey in surveys:
        data = data.append(df[df['familyCode'] == survey])

#make csv with family data
data.to_csv('familyCodes-Family.csv', index=False)