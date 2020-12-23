import pandas as pd

sheet = pd.read_excel("../Datasheets/svcategory-nocomma.xlsx")
df = pd.DataFrame(sheet, columns=['UNSPSC.AribaCategoryIdL3', 'UNSPSC.AribaCategoryL3', 'AccountingDate.Month1970', 'sum(Amount)', 'total_quantity'])

previd = -1

with open('../SQL Files/firstsheetinserts.sql', 'w') as f:
    for _, row in df.iterrows():

        commodityid = row['UNSPSC.AribaCategoryIdL3']
        month = row['AccountingDate.Month1970']
        amount = row['sum(Amount)']

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
