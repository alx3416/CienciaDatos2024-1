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
    # Hacer check sobre carpeta output
    # Deben guardarse los histogramas de todas las variables en imágenes separadas
    # Cada imagen se debe nombrar acorde a la variable utilizada
    pass


def save_correlation(data, var1, var2, corr_value):
    # check if output/scatterplots exist
    # create new fig
    # create scatterplot
    # save figure
    # close figure
    pass


def save_correlations(data, correlations):
    # create each scatter plot for var1 and var2
    # save each plot
    pass

def save_all_correlations(data, correlations):
    pass
