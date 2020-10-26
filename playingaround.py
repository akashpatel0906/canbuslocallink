import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server=app.server

app.layout = html.Div(
    [
        html.I("Try typing in input 1 & 2, and observe how debounce is impacting the callbacks. Press Enter and/or Tab key in Input 2 to cancel the delay"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder=""),
        html.Div(id="output")
    ]
)


@app.callback(Output("output", "children"),[Input("input1", "value")])
def update_output(input1):
    df=pd.read_csv(input1)
    fig = px.line(df, x = 'Timestamp', y = 'Value(DEC)', color='Name', title='CANBus Data Values')
    fig.show()
    return input1


if __name__ == "__main__":
    app.run_server(debug=True)
