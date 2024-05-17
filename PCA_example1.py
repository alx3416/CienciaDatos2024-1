import numpy as np
import math as mt
from sklearn.decomposition import PCA
import pandas as pd
import utils.processing as proc
import matplotlib.pyplot as plt

data = [[10, 6, 12, 5], [11, 4, 9, 7], [8, 5, 10, 6], [3, 3, 2.5, 2], [2, 2.8, 1.3, 4], [1, 1, 2, 7]]
df = pd.DataFrame(data, columns=['Gen1', 'Gen2', 'Gen3', 'Gen4'])
print(df)
print()
# Normalize data
df_norm = proc.normalize_gen_data(df)
print(df_norm)
print()

pca = PCA(n_components=2)
df_r = pca.fit(df_norm).transform(df_norm)
print(df_r)

plt.scatter(df_r[:, 0], df_r[:, 1])
plt.show()
