import pandas as pd

def open_file(path):
    data = pd.read_csv(path)
    return data.head()
