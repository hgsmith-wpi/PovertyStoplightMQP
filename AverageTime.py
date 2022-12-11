import pandas as pd
from datetime import datetime


df = pd.read_excel("familyCodes-Family.xlsx")

#names of the 16 organizations we are using as DMUs
organizationTotal = {'Aseguradora Tajy' : 0, 'Banco Da Familia' : 0, 'Banco Da Familia - Comunidades' : 0, 'Cadena Farmacenter': 0,
 'CENSU SA' : 0, 'Cervepar' : 0, 'Children International':0, 'Control Union Paraguay':0, 'DESEM':0, 'Díaz Gill':0, 'El Mejor':0,
  'Fundacion Naho':0, 'Grupo Dekalpar':0, 'JOBS':0, 'Minerva Foods':0, 'Usma Mañanitas':0}

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