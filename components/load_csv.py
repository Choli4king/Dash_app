#%%
'''
import base64
import datetime
import io
import csv
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd


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
                    'width': '98%',
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
    ]
)


""" uncomment this for running this file on its own for developement
app.layout = layout
"""


#%%


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



def parse_contents(file, filename, date):
    global df #global df this is to remove the (unbound error) that df causes

    content_type, content_string = file  #contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
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
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(file[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])



def prepared_csv(contents, filename):

    # read through a csv change the row you need to, then save it to a new file
    with open(contents, 'r') as f:
        reader = csv.reader(f, delimiter=',')

        title = next(reader) #get next item from reader
        lines = [] 

        for line in reader:    # line is a row in the csv file
            if len(line) == 9 and line[8] == ' Status':
                line.append('')
                
            lines.append(line)

    filename1 = filename + 'mti'        

    # save changes to new csv file    
    with open(filename1, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(title)
        writer.writerows(lines)

    csv_data = pd.read_csv(filename1, header=[0], skiprows=1, skip_blank_lines=True, encoding='utf-8')
    csv_data.columns = csv_data.columns.str.lstrip(' ')
    inplace = True 

    # Remember axis 1 = columns and axis 0 = rows.
    csv_data.drop(csv_data.columns[9], axis=1, inplace=True)
    #print(csv_data)

    return csv_data #returns dataframe




if __name__ == '__main__':
    app.run_server(debug=True)

'''