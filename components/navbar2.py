import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"


nav_item = dbc.NavItem(
        dbc.NavLink('MTI login', href='https://mymticlub.com/userpanel/login.php')
    
)

db = dbc.NavItem(
    dbc.NavLink('Dashboard', href='#'),
)

dropdown = dbc.DropdownMenu(children=[
        dbc.DropdownMenuItem('upload csv'),
        dbc.DropdownMenuItem('My Tree')
    ],
    nav=True,
    in_navbar=True,
    label='Menu'
)


navbar = dbc.Navbar(
    dbc.Container(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("MTI Stats", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            #href="https://plot.ly",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(dbc.Nav([nav_item, db, dropdown], className='ml-auto', navbar=True,), id="navbar-collapse", navbar=True),
    ],
    ),
    color="purple",
    dark=True,
    className='mb-5'
    
)

app.layout = html.Div(
    [
        navbar
    ]
)


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)