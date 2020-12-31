# Collocation v1 vs Collocation v2 vs Exact
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cem.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["Collocation 1"], name='Version 1'))
fig.add_trace(go.Scatter(x=df["x"], y=df["Collocation 2"], name='Version 2'))
fig.add_trace(go.Scatter(x=df["x"], y=df["ExactSolution"], name='Exact Solution'))
fig.update_layout(title_text="Plot between Exact solution & Collocation methods")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="Collocation and Exact")
fig.show()
