# Dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# Set seed
np.random.seed(42)
# Create random array of numbers
x = np.random.randn(500)
# Get histogram
fig = go.Figure(data=[go.Histogram(x=x)])

## DASHBOARD
# Get stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Initialize dashboard
app = dash.Dash()
# Create layout
app.layout = html.Div(children=[
    html.H1(children='A Histogram'),
    html.Div(children='''Of A Randomly Generated Number'''),
    dcc.Graph(figure = fig)
])
# Run
if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', debug=True)