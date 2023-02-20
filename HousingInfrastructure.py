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

#indicators that are in Housing & Infrastructure
enoughSpace = df['Enough space']
kitchen = df['Kitchen']
bathroom = df['Bathroom']
phone = df['Phone']
electricity = df['Electricity']
organizations = df['organizationName']

#add up each indicator changes per family
for i in range(0,len(enoughSpace),2):
    if organizationTotal.get(organizations[i]) != None:
        spaceDifference = enoughSpace[i+1] - enoughSpace[i]
        kitchenDifference = kitchen[i+1] - kitchen[i]
        bathroomDifference = bathroom[i+1] - bathroom[i]
        phoneDifference = phone[i+1] - phone[i]
        electricityDifference = electricity[i+1] - electricity[i]
        organizationTotal[organizations[i]] += (spaceDifference+kitchenDifference+bathroomDifference+phoneDifference+electricityDifference)
        organizationOccurences[organizations[i]] += 1
print(organizationTotal)

#divide by the amount of follow-up surveys
for organization in organizationTotal:
    organizationTotal[organization]  /= organizationOccurences[organization]
print(organizationTotal)