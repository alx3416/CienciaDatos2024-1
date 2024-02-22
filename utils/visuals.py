import seaborn as sns
import utils.processing as proc
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


def save_histogram(data, column):
    proc.check_output_folder("output/histograms")
    sns_plot = sns.histplot(data=data[column])
    fig = sns_plot.get_figure()
    fig.savefig("output/histograms/histogram_"+column+".png")
    plt.close()


def save_histograms(data):
<<<<<<< Updated upstream
    # Hacer check sobre carpeta output
    # Deben guardarse los histogramas de todas las variables en imágenes separadas
    # Cada imagen se debe nombrar acorde a la variable utilizada
=======
    proc.check_output_folder("output/histograms")
    for column in data.columns:
        save_histogram(data, column)


def save_correlation(data, var1, var2):
    # Verificar si la carpeta "output" existe, si no, crearla
    proc.check_output_folder("output/scatterplots")

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


def save_correlations(data, correlations):
    # create each scatter plot for var1 and var2
    # save each plot
    pass


def save_all_correlations(data, correlations):
    #checar si la carpeta output existe, si no, crearla
    proc.check_output_folder("output/correlations")
    #guardar todas las correlaciones en un solo archivo
    correlations.to_csv("output/correlations/all_correlations.csv")
    #crear el grafcio de correlaciones
    fig = px.imshow(correlations)
    #guardar todas las correlaciones en imágenes individuales png
    #Es importante evitar cifras duplicadas, la correlación A vs B es la misma que la correlación B vs A
    for i in range(correlations.shape[0]):
        for j in range(i, correlations.shape[1]):
            if i != j:
                save_correlation(data, correlations.columns[i], correlations.columns[j])
>>>>>>> Stashed changes
    pass
