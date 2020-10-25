import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_core_components


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

modal = html.Div(
    [
        dbc.Button("Extra large modal", id="open-xl"),
        dbc.Modal(
            [
                dbc.ModalHeader("Header"),
                dbc.ModalBody("An extra large modal."),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close-xl", className="ml-auto")
                ),
            ],
            id="modal-xl",
            size="xl",
        ),
    ]
)

app.layout = html.Div(
    [
        modal
    ]
)


def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


app.callback(
    Output("modal-xl", "is_open"),
    [Input("open-xl", "n_clicks"), Input("close-xl", "n_clicks")],
    [State("modal-xl", "is_open")],
)(toggle_modal)



if __name__ == "__main__":
    app.run_server(debug=True)