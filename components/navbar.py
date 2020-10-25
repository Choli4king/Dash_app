from os import link
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Load csv/xml", href="/1")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Tree", href="/2"),
                    dbc.DropdownMenuItem("Pie Chart", href="/3"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Dashboard",
        brand_href="/board",
        color="primary",
        dark=True,
)

""" uncomment this for running this file on its own for developement
app.layout = html.Div(
    [
        html.Div([
            Navbar()
        ], className="Row"),
        html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content', children=[])
        ], className='Row') 
    ]
)
"""

if __name__ == "__main__":
    app.run_server(debug=True)