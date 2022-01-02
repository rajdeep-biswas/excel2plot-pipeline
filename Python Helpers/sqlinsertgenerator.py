def generate_inserts(commodity, algorithm, forecastlength):

    """
    Params:
        commodity: the unique identifier for the commodity.
        algorithm: string identifier for which forecasting algorithm to use.
        forecastlength: the time window over which to forecast the results.
    Generates an .sql file solely for the INSERT queries of each individual commodity over each individual algorithm.
    """

    # Dictionary for holding the DB Table Identifier Strings
    tablenames = {
        "arima": "PAL_ARIMA_DATA_TBL",
        "autoarima": "PAL_ARIMA_DATA_TBL",
        "brown": "PAL_BROWNSMOOTH_DATA_TBL",
        "brownad": "PAL_BROWNSMOOTH_DATA_TBL",
        "croston": "PAL_CROSTON_DATA_TBL",
        "linreg": "PAL_FORECASTSLR_DATA_TBL",
        "singlesmooth": "PAL_SINGLESMOOTH_DATA_TBL",
        "doublesmooth": "PAL_DOUBLESMOOTH_DATA_TBL",
        "triplesmooth": "PAL_TRIPLESMOOTH_DATA_TBL"
    }
    
    filename = commodity + '-' + algorithm + ".sql"
    with open("../Datasheets/ByCategory/" + commodity + ".txt", 'r') as file:
        for line in file:
            points = line.split()

    if len(points) < 18:
        return False
    
    days = list(range(len(points)))
    with open("../Datasheets/Queries/" + filename, 'w') as file:
        for i in range(len(days) - forecastlength):
            file.write("INSERT INTO " + tablenames[algorithm] + " VALUES(" + str(days[i] + 1) + ", " + str(points[i]) + ");\n")

    print("Insert query file generated: " + filename)
    return True
