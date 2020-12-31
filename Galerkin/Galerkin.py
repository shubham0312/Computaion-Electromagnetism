# (Comparison between Galerkin and Exact Solutions)
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cem.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["Galerkin"], name='Galerkin'))
fig.add_trace(go.Scatter(x=df["x"], y=df["ExactSolution"], name='Exact Solution'))
fig.update_layout(title_text="Plot between Exact solution & Galerkin methods")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="Galerkin and Exact")
fig.show()
