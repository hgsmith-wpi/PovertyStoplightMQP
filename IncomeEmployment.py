import pandas as pd

df = pd.read_excel("familyCodes-Indicators.xlsx")

#total number of improvements for each organization
organizationTotal = {'Aseguradora Tajy' : 0, 'Banco Da Familia' : 0, 'Banco Da Familia - Comunidades' : 0, 'Cadena Farmacenter': 0,
 'CENSU SA' : 0, 'Cervepar' : 0, 'Children International':0, 'Control Union Paraguay':0, 'DESEM':0, 'Díaz Gill':0, 'El Mejor':0,
  'Fundacion Naho':0, 'Grupo Dekalpar':0, 'JOBS':0, 'Minerva Foods':0, 'Usma Mañanitas':0}

#number follow-up surveys from each organization
organizationOccurences = {'Aseguradora Tajy' : 0, 'Banco Da Familia' : 0, 'Banco Da Familia - Comunidades' : 0, 'Cadena Farmacenter': 0,
 'CENSU SA' : 0, 'Cervepar' : 0, 'Children International':0, 'Control Union Paraguay':0, 'DESEM':0, 'Díaz Gill':0, 'El Mejor':0,
  'Fundacion Naho':0, 'Grupo Dekalpar':0, 'JOBS':0, 'Minerva Foods':0, 'Usma Mañanitas':0}

#indicators that are in Income & Employment
income = df['Income']
savings = df['Savings']
credit = df['Credit']
organizations = df['organizationName']

#add up each indicator changes per family
for i in range(0,len(income),2):
    if organizationTotal.get(organizations[i]) != None:
        incomeDifference = income[i+1] - income[i]
        savingsDifference = savings[i+1] - savings[i]
        creditDifference = credit[i+1] - credit[i]
        organizationTotal[organizations[i]] += (incomeDifference+savingsDifference+creditDifference)
        organizationOccurences[organizations[i]] += 1
print(organizationTotal)

#divide by the amount of follow-up surveys
for organization in organizationTotal:
    organizationTotal[organization]  /= organizationOccurences[organization]
print(organizationTotal)