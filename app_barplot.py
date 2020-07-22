# Dependencies
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os
# Get data (originally from https://github.com/chris1610/pbpython/blob/master/data/salesfunnel.xlsx?raw=True)
df = pd.read_feather(os.path.join(os.getcwd(), "data", "sample_data.feather"))
# Pivot
pv = pd.pivot_table(df, index=['Name'], columns=["Status"], values=['Quantity'], aggfunc=sum, fill_value=0)
# Set up bar plots as plotly graph objects
trace1 = go.Bar(x=pv.index, y=pv[('Quantity', 'declined')], name='Declined')
trace2 = go.Bar(x=pv.index, y=pv[('Quantity', 'pending')], name='Pending')
trace3 = go.Bar(x=pv.index, y=pv[('Quantity', 'presented')], name='Presented')
trace4 = go.Bar(x=pv.index, y=pv[('Quantity', 'won')], name='Won')

## DASHBOARD
# Set stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# Initialize dashboard
app = dash.Dash()
# Set layout
app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4],
            'layout':
            go.Layout(title='Order Status by Customer', barmode='stack')
        })
])
# Run
if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', debug=True)
