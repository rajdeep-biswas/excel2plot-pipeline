import numpy as np
import csv

def mse_scores(commodity, y_dict):
    y_test = y_dict["real"]
    mse = {}

    for y in y_dict:
        if y != 'real':
            mse[round(sum((np.array(y_test[-6:]) - np.array(y_dict[y][-6:]))**2))] = y

    return mse

def assign_scores(mse):
    rev_rank = 100
    scored_alg = {}
    for score in sorted(mse):
        scored_alg[mse[score]] = rev_rank
        rev_rank -= 10

    return scored_alg

def update_scores(new_score, previous_score):
    print("\n***********\nNEW SCORES: ")
    print(new_score, end="\n\n")
    for alg in previous_score:
        new_score[alg] += previous_score[alg]
    print("CURRENT STANDINGS: ")
    print(new_score, end="\n***********\n\n")
    return [new_score, previous_score]

def write_score_csv(commodity, scores):
    with open("..\MSE_Log\performance.csv", "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([commodity.strip(), scores["arima"], scores["autoarima"], scores["brown"], scores["brownad"], scores["croston"], scores["linreg"], scores["singlesmooth"], scores["doublesmooth"], scores["triplesmooth"]])
