import pandas as pd

df = pd.read_excel("familyCodes-Indicators.xlsx")

#total number of improvements for each organization
organizationTotal = {'A' : 0, 'B' : 0, 'C' : 0, 'D': 0,
 'E' : 0, 'F' : 0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0,
  'L':0, 'M':0, 'N':0, 'O':0, 'P':0}

#number follow-up surveys from each organization
organizationOccurences = {'A' : 0, 'B' : 0, 'C' : 0, 'D': 0,
 'E' : 0, 'F' : 0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0,
  'L':0, 'M':0, 'N':0, 'O':0, 'P':0}

#indicators that are in education & culture
schooling = df['Schooling']
literacy = df['Literacy']
internet = df['Internet']
organizations = df['organizationName']

#add up each indicator changes per family
for i in range(0,len(schooling),2):
    if organizationTotal.get(organizations[i]) != None:
        schoolingDifference = schooling[i+1] - schooling[i]
        literacyDifference = literacy[i+1] - literacy[i]
        internetDifference = internet[i+1] - internet[i]
        organizationTotal[organizations[i]] += (schoolingDifference+literacyDifference+internetDifference)
        organizationOccurences[organizations[i]] += 1
print(organizationTotal)

#divide by the amount of follow-up surveys
for organization in organizationTotal:
    organizationTotal[organization]  /= organizationOccurences[organization]
print(organizationTotal)