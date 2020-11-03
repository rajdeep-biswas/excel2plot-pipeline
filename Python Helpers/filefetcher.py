from os import listdir

def get_commodities(filepath):
    return [file[:-4] for file in listdir(filepath)]
