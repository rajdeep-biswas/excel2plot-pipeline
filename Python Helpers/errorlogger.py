import numpy as np
import csv

SEQ_LENGTH = 6 # number of days to be predicted

def mse_scores(commodity, y_dict):
    """
    Params: 
        commodity: the unique identifier for the commodity.
        y_dict: a dictionary containing the predictions made by various algorithms, including the actual value denoted by a key string 'real'.
    Calculates the mean squared errors of each algorithm prediction and returns a reversed dictionary of keyed MSEs and valued algorithm.
    """
    y_test = y_dict["real"]
    mse = {}

    for y in y_dict:
        if y != 'real':
            mse[round(sum((np.array(y_test[-SEQ_LENGTH:]) - np.array(y_dict[y][-SEQ_LENGTH:]))**2))] = y

    return mse


def assign_scores(mse):
    """
    Params:
        mse: a dictionary of MSEs.
    Performs a custom scoring system is assigned by ranking the highest performing algorithm with a score of 100,
    and each subsequent algorithm gets a score lowered by 10 according to rank.
    """
    rev_rank = 100
    scored_alg = {}
    for score in sorted(mse):
        scored_alg[mse[score]] = rev_rank
        rev_rank -= 10

    return scored_alg


def update_scores(new_score, previous_score):
    """
    Params:
        new_score: a dictionary of updated scores of each algorithm.
        previous_score: a dictionary of previous recorded score of each algorithm.
    Updates the scores dictionary to and also displays them in comparison to the previous iteration on the CLI.
    """
    print("\n***********\nNEW SCORES: ")
    print(new_score, end="\n\n")
    for alg in previous_score:
        new_score[alg] += previous_score[alg]
    print("CURRENT STANDINGS: ")
    print(new_score, end="\n***********\n\n")
    return [new_score, previous_score]


def write_score_csv(commodity, scores):
    """
    Params:
        commodity: the unique identifier for the commodity.
        scores: dictionary containing the scores of each algorithm.
    Writes the scores of an iteration into a CSV file for future referral.
    """
    with open("..\MSE_Log\performance.csv", "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([commodity.strip(), scores["arima"], scores["autoarima"], scores["brown"], scores["brownad"], scores["croston"], scores["linreg"], scores["singlesmooth"], scores["doublesmooth"], scores["triplesmooth"]])
