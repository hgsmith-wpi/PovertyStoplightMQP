import pandas as pd
from datetime import datetime


df = pd.read_excel("familyCodes-Family.xlsx")

#names of the 16 organizations we are using as DMUs
organizationTotal = {'A' : 0, 'B' : 0, 'C' : 0, 'D': 0,
 'E' : 0, 'F' : 0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0,
  'L':0, 'M':0, 'N':0, 'O':0, 'P':0}

dates = df['surveyDate']
organizations = df['organizationName']
data = pd.DataFrame()

#get the responsiveness of each organization (time between each survey)
for i in range(0,len(df),2):
    if organizationTotal.get(organizations[i]) != None:
        date1 = datetime.strptime(str(dates[i]), '%Y-%m-%d %H:%M:%S')
        date2 = datetime.strptime(str(dates[i+1]), '%Y-%m-%d %H:%M:%S')
        organizationTotal[organizations[i]] +=  (date2-date1).days
        
#divide the total responsiveness by the amount of follow-up surveys from the organization
for org in organizationTotal:
    organizationTotal[org] = organizationTotal[org]/(organizations == org).sum()
    
print(organizationTotal)