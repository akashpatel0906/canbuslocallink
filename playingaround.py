from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://filebin.net/n23827xxj36naw6o']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

df = pd.read_csv('/Users/akashpatel/Documents/FormulaTest/testnew.csv')

fig = px.line(df, x = 'Timestamp', y = 'Value(DEC)', color='Name', title='CANBus Data Values')

app.layout = html.Div(children=[
    html.H2(children='CANBus Grapher'),

    html.Div(children='''
        Made by Illini Formula Electric.
    '''),

    dcc.Graph(
        id='example-graph',
        
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


