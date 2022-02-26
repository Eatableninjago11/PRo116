import plotly.express as px
import csv
import pandas as pd


df = pd.read_csv("data_classification.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
GRE_Score = df["GRE Score"].tolist()

fig = px.scatter(x= TOEFL_Score, y=GRE_Score)
fig.show()


import plotly.graph_objects as go

hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()

results = df["results"].tolist()
colors=[]
for data in results:
  if data == 1:
    colors.append("green")
  else:
    colors.append("red")



fig = go.Figure(data=go.Scatter(
    x=hours_studied,
    y=hours_slept,
    mode='markers',
    marker=dict(color=colors)
))
fig.show()