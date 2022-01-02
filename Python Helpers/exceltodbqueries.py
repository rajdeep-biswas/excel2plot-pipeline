import pandas as pd

"""
There are certain parts labelled out as configuration in the HANA stored procedure .sql files.
This part of the code is to programmatically replace those with dynamic INSERT queries.
"""

sheet = pd.read_excel("../Datasheets/svcategory-nocomma.xlsx")
df = pd.DataFrame(sheet, columns=['UNSPSC.AribaCategoryIdL3', 'UNSPSC.AribaCategoryL3', 'AccountingDate.Month1970', 'sum(Amount)', 'total_quantity'])

previd = -1

CATEGORY_COL_NAME = 'UNSPSC.AribaCategoryIdL3'
MONTH_COL_NAME = 'AccountingDate.Month1970'
AMOUNT_COL_NAME = 'sum(Amount)'

with open('../SQL Files/firstsheetinserts.sql', 'w') as f:
    for _, row in df.iterrows():

        commodityid = row[CATEGORY_COL_NAME]
        month = row[MONTH_COL_NAME]
        amount = row[AMOUNT_COL_NAME]

        if previd == -1:
            previd = commodityid
            timestamp = 1

        if commodityid != previd:
            timestamp = 1

        f.write("INSERT INTO PAL_GENERIC_DATA_TBL VALUES("
            + str(timestamp) + ", '"
            + str(commodityid) + "', "
            + str(month) + ", "
            + str(amount) + ");\n")

        previd = commodityid
        
        timestamp += 1
