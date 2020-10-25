import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import base64
import datetime
import io
import dash_table
from pandas import DataFrame as df

from apps import import_csv
from apps.import_csv import Csv
from apps.card_modal import Card
from apps.navbar import Navbar


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


csv = Csv()
card = Card()


""" could be done this way using rows and col like this
app.layout = html.Div(
    [
        dbc.Row([
            Navbar
        ]),
        dbc.Row([
            dbc.Col([
                card
                ])
            ])
    ]
)
"""

# Although this is better for HTML5 five
app.layout = html.Div(
    [
        html.Div([
            Navbar()
        ], className="Row"),
        html.Div([
            dcc.Location(id='url', refresh=False), # the 'pathname' variable for dcc is empty by default
            html.Div(id='page-content', children=[])
        ], className='Row') 
    ]
)


#toggle pages callback
@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')], # we use pathname because it stores the last href
)
def display_page(pathname):
    if pathname == 'board':
        return card
    if pathname == '/1':
        return csv    
    if pathname == '/2':
        return card


#csv to dataframe uploader
@app.callback(Output('output-data-upload', 'children'),
            [Input('upload-data', 'contents')],
            [State('upload-data', 'filename'),
            State('upload-data', 'last_modified')]
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            import_csv.parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

#card_modal
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

if __name__ == "__main__":
    app.run_server(debug=True)