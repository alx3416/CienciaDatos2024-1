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
    # check if output folder exist
    # save correlation data in csv
    pass


def get_correlations(data):
    # obtain correlation data from dataframe
    # call save function
    # return correlations dataframe
    pass


def normalize_diabetes_data(data):
    # formula ->  Z = (1/sqrt(n)) * ((x-mu)/std)
    # apply to every column except Y
    # compare with diabetes normalized data to check
    # return Z
    pass