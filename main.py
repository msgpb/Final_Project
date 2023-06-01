import pandas as pd
import matplotlib.pyplot as plt
import requests

df = pd.read_csv('Untitled spreadsheet - Sheet1.csv')
df.plot()
print(df)

plt.show()