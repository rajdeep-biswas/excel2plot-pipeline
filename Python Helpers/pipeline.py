from filefetcher import get_commodities
from hdbpipeline import fetch_forecast
from sqlinsertgenerator import generate_inserts
from plotter import plot_all

commodities = get_commodities("../Datasheets/ByCategory/")
algorithms = ["arima", "brown", "brownad", "croston", "linreg", "singlesmooth", "doublesmooth", "triplesmooth"]
forecastlength = 6

plotrun = input('Jump to where you left off? ("yes" to activate): ')

for commodity in commodities:
    y_preds = {}
    generated = True
    for algorithm in algorithms:
        if not generate_inserts(commodity, algorithm, forecastlength):
            print(commodity + " dataset too small. Skipping to next.")
            generated = False
            break
        insertfile = commodity + '-' + algorithm + '.sql'
        dbpipefile = algorithm + 'pipeline.sql'
        if plotrun == 'yes':
            y_preds[algorithm] = fetch_forecast(insertfile, dbpipefile, forecastlength, plotrun = True)
        else:
            y_preds[algorithm] = fetch_forecast(insertfile, dbpipefile, forecastlength)
    if generated:
        plot_all(commodity, y_preds, algorithms, begins = -1)
