import seaborn as sns
import utils.processing as proc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import os


def save_histogram(data, column):
    proc.check_output_folder("output/histograms")
    sns_plot = sns.histplot(data=data[column])
    fig = sns_plot.get_figure()
    fig.savefig("output/histograms/histogram_"+column+".png")
    plt.close()


def save_histograms(data):
    # Hacer check sobre carpeta output
    # Deben guardarse los histogramas de todas las variables en imágenes separadas
    # Cada imagen se debe nombrar acorde a la variable utilizada
    pass


def save_correlation(data, var1, var2):
        # Verificar si la carpeta "output" existe, si no, crearla
        if not os.path.exists("output"):
            os.makedirs("output")

        # Calcular la correlación entre las dos variables
        correlation_value = data[var1].corr(data[var2])

        # Crear el gráfico de correlación
        sns.scatterplot(data=data, x=var1, y=var2)

        # Añadir el valor de correlación como parte del título
        plt.title(f"Correlación entre {var1} y {var2}: {correlation_value}")
        plt.xlabel(var1)
        plt.ylabel(var2)

        # Guardar el gráfico como imagen PNG
        plt.savefig(f"output/scatterplots/{var1}_{var2}_correlation_plot.png")

        # Limpiar la figura
        plt.clf()
        plt.close()
        pass


def save_correlations(data, correlations):
    # create each scatter plot for var1 and var2
    # save each plot
    pass

def save_all_correlations(data, correlations):
    pass
