'''
Ideabytes Inc
Author : Suman
Date: 30/dec/2020
'''


import pandas as pd
file_path = "D:\\HDF\\Abhilash\\IB Cucumber.csv"
data = pd.read_csv(file_path)


al = dict()
header = data.columns
ps = ''
cm = ''
ss = ''
cl = ''
bl = ''
chl = ''
se = ''
cnt=1
psl=[]
cml=[]
ssl=[]
cll=[]
bll=[]
chll=[]
sel=[]
for row_num  in range(0,len(data)):


    if str(data['PEST/DISEASES NAME'][row_num])=='nan':



        SYMPTOMS = str(data['SYMPTOMS'][row_num])
        if SYMPTOMS=='nan':
            SYMPTOMS=''
        ss=ss+" "+SYMPTOMS
        CULTURAL_CONTROL = str(data['CULTURAL CONTROL'][row_num])
        if CULTURAL_CONTROL=='nan':
            CULTURAL_CONTROL=''
        CULTURAL_CONTROL = str(cl+" "+CULTURAL_CONTROL)
        BIOLOGICAL_CONTROL = str(data['BIOLOGICAL CONTROL'][row_num])
        if BIOLOGICAL_CONTROL=='nan':
            BIOLOGICAL_CONTROL=''
        bl = bl+" "+BIOLOGICAL_CONTROL
        CHEMICAL_CONTROL = str(data['CHEMICAL CONTROL'][row_num])
        if CHEMICAL_CONTROL=='nan':
            CHEMICAL_CONTROL = ''
        chl = chl+" "+CHEMICAL_CONTROL
        cnt=2

    else:
        if cnt==2:
            psl.append(ps)
            cml.append(cm)
            ssl.append(ss)
            cll.append(cl)
            bll.append(bl)
            chll.append(chl)
            sel.append(se)
            ps = ''
            cm = ''
            ss = ''
            cl = ''
            bl = ''
            chl = ''
            se = ''







        PEST = data['PEST/DISEASES NAME'][row_num]
        ps = str(PEST)
        CAUSAL_ORGANISM = data['CAUSAL ORGANISM'][row_num]
        cm=str(CAUSAL_ORGANISM)
        SYMPTOMS = data['SYMPTOMS'][row_num]
        ss=str(SYMPTOMS)
        CULTURAL_CONTROL = data['CULTURAL CONTROL'][row_num]
        cl=str(CULTURAL_CONTROL)
        BIOLOGICAL_CONTROL = data['BIOLOGICAL CONTROL'][row_num]
        bl=str(BIOLOGICAL_CONTROL)
        CHEMICAL_CONTROL = data['CHEMICAL CONTROL'][row_num]
        chl=str(CHEMICAL_CONTROL)
        STAGE_OCCURENCE = data['STAGE OF OCCURRENCE'][row_num]
        se=str(STAGE_OCCURENCE)

# dictionary of lists
dict = {'PEST/DISEASES NAME': psl, 'CAUSAL ORGANISM': cml, 'SYMPTOMS': ssl,'CULTURAL CONTROL':cll,'BIOLOGICAL CONTROL':bll,'CHEMICAL CONTROL':chll,'STAGE OF OCCURRENCE':sel}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('D:\\HDF\\Abhilash\\cucumber.csv')






