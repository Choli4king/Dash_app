import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
from components import csv_clean


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card1 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Daily ROI", className="card-title"),
                html.P(csv_clean.sum_roi_income(),
                        className="card-text",
                ),
                dbc.Button("info", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)

app.layout = html.Div(
    [
        card1
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)