import matplotlib.pyplot as plt
import pandas as pd

def clean_preds(commodity, y_preds):
    with open("../Datasheets/ByCategory/" + commodity + ".txt", 'r') as file:
        for line in file:
            y_test = [float(item) for item in line.split()]

    y_dict = {}

    for y_pred_alg in y_preds:
        
        if y_pred_alg in ["arima", "autoarima"]:
            y_pred = y_test[: -len(y_preds[y_pred_alg])] + y_preds[y_pred_alg]

        elif y_pred_alg in ["brown", "brownad", "singlesmooth", "doublesmooth"]:
            y_pred = [y_test[0]] + y_preds[y_pred_alg]

        elif y_pred_alg in ["triplesmooth"]:
            y_pred = [y_test[0]] * 4 + y_preds[y_pred_alg]

        elif y_pred_alg in ["croston", "linreg"]:
            y_pred = y_preds[y_pred_alg]

        y_dict[y_pred_alg] = y_pred

    # real values appended at last
    y_dict["real"] = y_test
    
    return y_dict

def plot_all(commodity, y_dict, begins = -1):

    y_test = y_dict["real"]
    mse = {}
    
    if begins == -1:
        begins = len(y_test) - 12

    x = list(range(1, len(y_test) + 1))

    for y in y_dict:
        plt.plot(x[begins:], y_dict[y][begins:])
        
    legend = list(y_dict.keys())

    plt.legend(legend)
    plt.title(commodity)
    plt.vlines(x = [len(x) - 6], ymin = 0, ymax = max(y_test), linestyles='dotted')
    
    plt.savefig("../PAL_Output_Plots/" + commodity + ".png", dpi = 200)
    # plt.show()
    print("Plot generated for " + commodity)
    plt.close()
