import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import serial
import time


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

ser = serial.Serial('/dev/cu.usbserial-14110', 9600, timeout=1)
ser.flush()

data = {
    'index': [],
    'celsius': [],
    'fahrenheit':[]
}
row_list = []

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H4('Simple Python Arduino Integration'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=2000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    global ser
    ser.write(b'1')
    line = ser.readline()
    row = line.decode('unicode_escape')

    row_list = row.split(',')
    
    
    if len(row_list) == 3:
        index = row_list[0]
        celsius = row_list[1]
        fahrenheit = row_list[2]

        data['index'].append(index)
        data['celsius'].append(celsius)
        data['fahrenheit'].append(fahrenheit)
    else:
        index = -1
        celsius = -1
        fahrenheit = -1
    

    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Index: '+str(index), style=style),
        html.Span('Celsius: '+str(celsius), style=style),
        html.Span('Fahrenheit: '+str(fahrenheit), style=style)
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': data['index'],
        'y': data['celsius'],
        'name': 'Celsius',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 1, 1)
    fig.append_trace({
        'x': data['index'],
        'y': data['fahrenheit'],
        'name': 'Fahrenheit',
        'mode': 'lines+markers',
        'type': 'scatter'
    }, 2, 1)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)