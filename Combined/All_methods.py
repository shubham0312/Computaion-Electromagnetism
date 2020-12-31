# Comparison of all the methods


import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cem.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["Least Squares"], name='Least Squares'))
fig.add_trace(go.Scatter(x=df["x"], y=df["Subdomain"], name='Subdomain'))
fig.add_trace(go.Scatter(x=df["x"], y=df["Galerkin"], name='Galerkin'))
fig.add_trace(go.Scatter(x=df["x"], y=df["Collocation 1"], name='Collocation Ver 1'))
fig.add_trace(go.Scatter(x=df["x"], y=df["Collocation 2"], name='Collocation Ver 2'))
fig.add_trace(go.Scatter(x=df["x"], y=df["ExactSolution"], name='Exact Solution'))
fig.update_layout(title_text="Plot between Exact solution & all four methods")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="Different methods")
fig.show()
