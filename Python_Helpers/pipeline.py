from filefetcher import get_commodities
from hdbpipeline import fetch_forecast
from sqlinsertgenerator import generate_inserts
from plotter import clean_preds, plot_all
from errorlogger import mse_scores, assign_scores, update_scores, write_score_csv

"""
This is the main driver file that runs the pipeline start to finish.
Possesses the capability to resume tasks from where it was left off in case of interruption(s).
"""

commodities = get_commodities("../Datasheets/ByCategory/")
algorithms = ["arima", "autoarima", "brown", "brownad", "croston", "linreg", "singlesmooth", "doublesmooth", "triplesmooth"]
forecastlength = 6

plotrun = input('Jump to where you left off? ("yes" to activate): ')

scores = {"arima": 0, "autoarima": 0, "brown": 0, "brownad": 0, "croston": 0, "linreg": 0, "singlesmooth": 0, "doublesmooth": 0, "triplesmooth": 0}
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
        y_dict = clean_preds(commodity, y_preds)
        plot_all(commodity, y_dict, begins = -1)
        mse = mse_scores(commodity, y_dict)
        scored_alg = assign_scores(mse)
        [scores, single_score] = update_scores(scored_alg, scores)
        write_score_csv(commodity, single_score)
