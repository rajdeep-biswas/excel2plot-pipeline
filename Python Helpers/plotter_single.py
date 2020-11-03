import matplotlib.pyplot as plt
import pandas as pd

comid = "100003-complete-72"
meancolindex = 1

pointstrained = 66

with open("../Datasheets/ByCategory/" + comid + ".txt", 'r') as file:
    for line in file:
        y_test = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-arima" + ".txt", 'r') as file:
    for line in file:
       arima_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-brown" + ".txt", 'r') as file:
    for line in file:
       brown_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-brownad" + ".txt", 'r') as file:
    for line in file:
       brownad_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-croston" + ".txt", 'r') as file:
    for line in file:
       croston_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-singlesmooth" + ".txt", 'r') as file:
    for line in file:
       singlesmooth_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-doublesmooth" + ".txt", 'r') as file:
    for line in file:
       doublesmooth_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-triplesmooth" + ".txt", 'r') as file:
    for line in file:
       triplesmooth_y_pred = [float(item) for item in line.split()]

with open("../Datasheets/Forecasts/" + "100003-complete-72-linreg" + ".txt", 'r') as file:
    for line in file:
       linreg_y_pred = [float(item) for item in line.split()]

x = list(range(1, len(y_test) + 1))
