import os
import math as mt
import pandas as pd


def check_output_folder(path):
    if os.path.isdir(path):
        pass
    else:
        os.makedirs(path)
        print(path + " folder created")
