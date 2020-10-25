

import  importlib
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
from pandas import DataFrame as df

# Connect to main app.py file
from app import app, server

# connect to your apps directory to import your components
from components import import_csv_std2, navbar


#app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

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
            navbar.layout
        ], className="Row"),
        html.Div([
            dcc.Location(id='url', refresh=False), # the unseen 'pathname' variable in this line for dcc is empty by default
            html.Div(id='page-content', children=[])
        ], className='Row') 
    ]
)


#toggle pages callback
@app.callback(Output(component_id='page-content', component_property='children'),
            [Input(component_id='url', component_property='pathname')], # we use pathname because it stores the last href
)
def display_page(pathname):
    if pathname == '/board':
        from components import card_modal, charts
        return card_modal.layout, charts.layout
    if pathname == '/1':
        return import_csv_std2.layout    
    if pathname == '/2':
        return " Tree coming soon"
    if pathname == '/3':
        return "Pie charts coming soon"
    else:
        return "404"   


#csv to dataframe uploader
@app.callback(Output('output-data-upload', 'children'),
            [Input('upload-data', 'contents')],
            [State('upload-data', 'filename'),
            State('upload-data', 'last_modified')]
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            import_csv_std2.parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

#card_modal
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

app.callback(
    Output("modal-1", "is_open"),
    [Input("open-1", "n_clicks"), Input("close-1", "n_clicks")],
    [State("modal-1", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-2", "is_open"),
    [Input("open-2", "n_clicks"), Input("close-2", "n_clicks")],
    [State("modal-2", "is_open")],
)(toggle_modal)

app.callback(
    Output("modal-3", "is_open"),
    [Input("open-3", "n_clicks"), Input("close-3", "n_clicks")],
    [State("modal-3", "is_open")],
)(toggle_modal)    

if __name__ == "__main__":
    app.run_server(debug=True)