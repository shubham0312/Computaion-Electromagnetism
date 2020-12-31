# Subdomain vs Exact Solution
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('cem.csv')

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["x"], y=df["Subdomain"], name='Subdomain'))
fig.add_trace(go.Scatter(x=df["x"], y=df["ExactSolution"], name='Exact Solution'))
fig.update_layout(title_text="Plot between Exact solution & Subdomain methods")
fig.update_xaxes(title_text="x")
fig.update_yaxes(title_text="Subdomain and Exact")
fig.show()
