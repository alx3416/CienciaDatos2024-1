import pandas as pd


def read_diabetes_dataset(path):
    # Utilizar pandas para cargar el txt como objeto dataframe
    data = pd.read_csv(path, sep="\t")
    return data

#Read the file .xlsx
def read_excel(path):
    # Utilizar pandas para cargar el txt como objeto dataframe
    data = pd.read_excel(path)
    return data

#printeamos todos los archivos de un directorio
def print_files_in_directory(path):
    import os
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            print(os.path.join(dirname, filename))

def read_csv_tomates(path):
    # Utilizar pandas para cargar el txt como objeto dataframe
    data = pd.read_csv(path)
    return data
