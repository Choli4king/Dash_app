
import base64
import datetime
import io
import os

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table


import pandas as pd 
from pandas import DataFrame
import csv

from components import prepared_csv2 as pc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])

def save_csv(filename):
    location = ("E:/Documents/Programming/Python/Dash_app/components/{}").format(filename)
    #print(location)
    return location

def new_save_csv(filename):
    location = ("E:/Documents/Programming/Python/Dash_app/components/new_{}").format(filename)
    #print(location)
    return location    

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',') # splits a string into a list

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            #df = pd.read_csv(io.StringIO(decoded.decode('utf-8'))) #read_csv converts to a df & StringIO() treats variable like a file
            #new_csv = df.to_csv("E:/Documents/Programming/Python/Dash_app/components/{}".format(filename), index=False, header=True)
            
            #print(contents) # = prepared_csv(df)
            #print(io.StringIO(decoded.decode('utf-8'))) # = prepared_csv(df)
            location = save_csv(filename)
            global location2
            location2 = new_save_csv(filename)

            #data = .getvalue()
            data = io.StringIO(decoded.decode('utf-8'))
            #print(data.getvalue())
            data = pd.read_csv(io.StringIO(decoded.decode('utf-8')), index_col= False, skiprows=[0], skipinitialspace=True)
            #print(data)
            data.to_csv(location, index=False)
                        
            #print(csv_data)
            #print(location) # = prepared_csv(df)
            #print(new_csv) # = prepared_csv(df)
            
            df = pc.prepared_csv(location, location2)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        

        dash_table.DataTable(
            data = df.to_dict('records'),
            columns = [{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])



@app.callback(Output('output-data-upload', 'children'),
            [Input('upload-data', 'contents')],
            [State('upload-data', 'filename'),
            State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]    
        return children     


if __name__ == '__main__':
    app.run_server(debug=True)
