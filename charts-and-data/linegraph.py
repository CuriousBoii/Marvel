import pandas as pd
from matplotlib import pyplot as plt


import os

cwd = os.getcwd()  # Get the current working directory (cwd)

thisDir = cwd+'\Documents\MARVEL-UVCE\charts-and-data'  # Get all the files in that directory


data = pd.read_excel(thisDir + '\GovernmentSpendingPerCapita.xlsx')
print(data.STATES)
plt.plot(data.STATES, data.POPULATION/ 10**7, 'o')
plt.xlabel("states")
plt.ylabel("population")
plt.show()

