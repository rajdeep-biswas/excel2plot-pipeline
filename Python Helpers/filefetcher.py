from os import listdir

def get_commodities(filepath):
    """
    Omits the extension of a filename and gets all commodity files under the stored folder.
    """
    return [file[:-4] for file in listdir(filepath)]
