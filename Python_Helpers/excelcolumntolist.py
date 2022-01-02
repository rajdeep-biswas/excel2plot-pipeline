import pandas as pd

"""
This file does the hard work of figuring out the unique commodities across the excel sheet and writing the expense values into individual .txt files.
This can be made much simpler by just using the `DataFrame.groupby` method but I was too early in my career to have known that (this documentation is 1+ year in the future of when this code was written).
"""

sheet = pd.read_excel("../Datasheets/svcategory-nocomma.xlsx")
df = pd.DataFrame(sheet, columns=['UNSPSC.AribaCategoryIdL3', 'UNSPSC.AribaCategoryL3', 'AccountingDate.Month1970', 'sum(Amount)', 'total_quantity'])

# Some variables that help to keep track of whether there is a new commodity in the current iteration and also the last category that was checked.
# The latter is to resolve the same commodity over different sheets in the excel file.

lastcategory = -1
lastmonth = -1
values = []
compflag = True
count = 0

CATEGORY_COL_NAME = 'UNSPSC.AribaCategoryIdL3'
MONTH_COL_NAME = 'AccountingDate.Month1970'

for _, row in df.iterrows():
    category = row[CATEGORY_COL_NAME]
    month = row[MONTH_COL_NAME]

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
