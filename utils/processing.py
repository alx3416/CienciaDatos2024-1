import os
import math as mt
import pandas as pd


def check_output_folder(path):
    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path)
        print(path + " folder created")


def save_correlations(data):
    check_output_folder("output")
    correlations = data.corr()
    # Guardar las correlaciones en un archivo CSV
    correlations.to_csv("output/correlations.csv")
    print("Correlation data saved as 'output/correlations.csv'")


def get_correlations(data):
    # Calcular las correlaciones
    correlations = data.corr()

    # Guardar las correlaciones en un archivo CSV
    save_correlations(data)

    # Devolver el dataframe de correlaciones
    return correlations


def normalize_diabetes_data(data):
    # formula ->  Z = (1/sqrt(n)) * ((x-mu)/std)
    mu_data = data.mean()
    std_data = data.std()
    normalized_data = data.sub(mu_data, axis='columns')
    normalized_data = normalized_data.div(std_data, axis='columns')
    val = (1 / mt.sqrt(data.shape[0]))
    normalized_data = normalized_data.mul(val, axis='columns')
    normalized_data["Y"] = data["Y"]
    return normalized_data
