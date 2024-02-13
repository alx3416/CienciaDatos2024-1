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
    # Verificar si la carpeta "output" existe, si no, crearla
    check_output_folder("output")

    # Calcular las correlaciones
    correlations = data.corr()

    # Guardar las correlaciones en un archivo CSV
    correlations.to_csv("output/correlations.csv")
    print("Correlation data saved as 'output/correlations.csv'")
    pass


def get_correlations(data):
    # Calcular las correlaciones
    correlations = data.corr()

    # Guardar las correlaciones en un archivo CSV
    save_correlations(data)

    # Devolver el dataframe de correlaciones
    return correlations
    pass


def normalize_diabetes_data(data):
    # formula ->  Z = (1/sqrt(n)) * ((x-mu)/std)
    # apply to every column except Y
    # compare with diabetes normalized data to check
    # return Z
    pass