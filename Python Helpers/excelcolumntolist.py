import pandas as pd

sheet = pd.read_excel("../Datasheets/svcategory-nocomma.xlsx")
df = pd.DataFrame(sheet, columns=['UNSPSC.AribaCategoryIdL3', 'UNSPSC.AribaCategoryL3', 'AccountingDate.Month1970', 'sum(Amount)', 'total_quantity'])

lastcategory = -1
lastmonth = -1
values = []
compflag = True
count = 0

for _, row in df.iterrows():
    category = row['UNSPSC.AribaCategoryIdL3']
    month = row['AccountingDate.Month1970']

    if lastcategory == -1:
        lastcategory = category
        lastmonth = month
        
    if category != lastcategory:
        filename = str(lastcategory)
        if compflag:
            filename += "-complete"
        with open("../Datasheets/ByCategory/" + filename + '-' + str(count) + ".txt", 'w') as f:
            f.write(' '.join(values))
        lastcategory = category
        lastmonth = month
        values = []
        compflag = True
        count = 0
    
    values.append(str(row['sum(Amount)']))
        
    if month - lastmonth > 1:
        compflag = False

    lastmonth = month
    count += 1
