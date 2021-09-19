import plotly.express as px
import pandas as pd
import csv

df=pd.read_csv("Data.csv")
fig=px.scatter(df,x="date",y="cases",color="country")
fig.show()