import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_excel('../GovernmentSpendingPerCapita.xlsx')
print(data.STATES)
plt.plot(data.STATES, data.POPULATION/ 10**7, 'o')
plt.xlabel("states")
plt.ylabel("population")
plt.show()

