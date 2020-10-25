import dash
import dash_bootstrap_components as dbc

#BS = 'https://startbootstrap.com/themes/sb-admin-2'

#meta tags are to ensure program runs on mobile device
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content':'width=device-width, initial-scale=1.0'}]
)

server = app.server

#[dbc.themes.SOLAR]