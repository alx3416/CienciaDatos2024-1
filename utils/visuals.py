import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


def save_histogram(data, column):
    # Si no existe carpeta output una rutina debe checar si existe
    # y crearla de ser necesario
    # Debe generarse un histograma con seaborn o matplotlib y guardarse como imagen PNG
    # El nombre del archivo debe ser la variable/columna utilizada
    raise NotImplementedError


def save_histograms(data):
    # Hacer check sobre carpeta output
    # Deben guardarse los histogramas de todas las variables en imágenes separadas
    # Cada imagen se debe nombrar acorde a la variable utilizada
    raise NotImplementedError
