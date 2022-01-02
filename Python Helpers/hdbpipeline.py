from hdbcli import dbapi
from hdbcli.dbapi import Error

"""
Connects to a remote HANA Db Runtime in order to use the PAL library, execute the stored procedures from the SQL files, 
get the forecast results from each algorithm, and finally save the results into files for future referral.
(This step requires access to the company VPN).
"""

def fetch_forecast(insertqueries, allqueries, forecastlength, plotrun = False):
    
    try:
        with open("../Datasheets/Forecasts/" + insertqueries[:-4] + ".txt", 'r') as file:
            for line in file:
                y_pred = [float(item) for item in line.split()]
        if plotrun:
            choice = 'y'
        else:
            choice = input("File found. Use it (y). Fresh query database (n): ")
        
        if choice == 'y':
            return y_pred
        
    except FileNotFoundError:
        print("File not found. Connecting to database.")
            
    try:
        conn = dbapi.connect(
            address='hana161.lab1.ariba.com',
            port=30015,
            user='paltest',
            password='Paltest123'
        )
    except Error:
        print("Failed to connect to HANA. Terminating app.")
        exit()

    print('HDB connected')

    sqlqueries = ""
    with open("../Datasheets/Queries/" + insertqueries, 'r') as file:
        for line in file:
            sqlqueries += line

    allcommands = ""
    cursor = conn.cursor()
    with open("../SQL Files/" + allqueries, 'r') as file:
        for line in file:
            if line != "":
                allcommands += line.replace("INSERT_QUERIES_GO_HERE", sqlqueries).replace("FORECAST_LENGTH_GOES_HERE", str(forecastlength))

    print("Executing SQL for " +  allqueries)
        
    for line in allcommands.split("\n"):
        print(end=".")
        try:
            cursor.execute(line)
        except Error:
            print(line, end=": ")
            print(Error)
            continue
        conn.commit()

    print()
    y_pred = []
    rows = cursor.fetchall()
    for row in rows:
        y_pred.append(str(row[1]))

    with open("../Datasheets/Forecasts/" + insertqueries[:-4] + ".txt", 'w') as file:
        file.write(" ".join(y_pred))

    print("Forecast saved for " + allqueries)
    return y_pred
