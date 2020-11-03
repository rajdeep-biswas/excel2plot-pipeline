import matplotlib.pyplot as plt
import pandas as pd

comid = "100003-complete-72"
meancolindex = 1

pointstrained = 66

with open("../Datasheets/ByCategory/" + comid + ".txt", 'r') as file:
    for line in file:
        y_test = [float(item) for item in line.split()]

y_pred_arima = y_test[:pointstrained]
addpoints_arima = len(y_test) - pointstrained + 1
count_arima = 1

y_pred_brown = y_test[:1]
addpoints_brown = len(y_test)
count_brown = 1

y_pred_brown_adaptive = y_test[:1]

y_pred_croston_sporadic = []
y_pred_croston_constant = []
count_croston = 0

arima_sheet = pd.read_excel("../PAL_Output_Sheets/" + comid + "-arima.xlsx", header=None)
arima_df = pd.DataFrame(arima_sheet)

brown_sheet = pd.read_excel("../PAL_Output_Sheets/" + comid + "-brown.xlsx", header=None)
brown_df = pd.DataFrame(brown_sheet)

brown_adaptive_sheet = pd.read_excel("../PAL_Output_Sheets/" + comid + "-brown_adaptive.xlsx", header=None)
brown_adaptive_df = pd.DataFrame(brown_adaptive_sheet)

croston_sporadic_sheet = pd.read_excel("../PAL_Output_Sheets/" + comid + "-croston_sporadic.xlsx", header=None)
croston_sporadic_df = pd.DataFrame(croston_sporadic_sheet)

croston_constant_sheet = pd.read_excel("../PAL_Output_Sheets/" + comid + "-croston_sporadic.xlsx", header=None)
croston_constant_df = pd.DataFrame(croston_constant_sheet)

for _, row in arima_df.iterrows():
    y_pred_arima.append(float(row[meancolindex]))

for _, row in brown_df.iterrows():
    y_pred_brown.append(float(row[meancolindex]))
    
for _, row in brown_adaptive_df.iterrows():
    y_pred_brown_adaptive.append(float(row[meancolindex]))

for _, row in croston_sporadic_df.iterrows():
    y_pred_croston_sporadic.append(float(row[meancolindex]))

for _, row in croston_constant_df.iterrows():
    y_pred_croston_constant.append(float(row[meancolindex]))

x = list(range(1, len(y_test) + 1))
plt.plot(x, y_pred_arima)
plt.plot(x, y_pred_brown)
plt.plot(x, y_pred_brown_adaptive)
plt.plot(x, y_pred_croston_sporadic)
plt.plot(x, y_pred_croston_constant)
plt.plot(x, y_test)
plt.legend(["arima", "brown", "brown adaptive", "croston sporadic", "croston constant", "real"])
plt.savefig("../PAL_Output_Plots/" + comid + ".png")
plt.show()
