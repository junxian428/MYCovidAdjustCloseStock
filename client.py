from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()
df = pd.read_csv("klse.csv")
df.plot(x="Date",y="Adj Close",ax=ax)


#https://flevy.com/coronavirus/malaysia
df2 = pd.read_csv("coronavirus.csv")
df2.plot(x="Date",y="New Cases",ax=ax , secondary_y=True)

plt.show()