import pandas as pd


def read_diabetes_dataset(path):
    # Utilizar pandas para cargar el txt como objeto dataframe
    data = pd.read_csv(path, sep="\t")
    return data

def read_inegi_datset(path):
    data2 =pd.read_csv(path, sep="\t")
    return data2
