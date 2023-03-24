import pandas as pd
from matplotlib import pyplot as plt

timedata = {'facebook':120,'instagram':40, 'snapchat':28, 'youtube':90}
platforms = timedata.keys()
time = timedata.values()
plt.bar(platforms, time, color = 'maroon')
plt.show()