# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#import os 
#import sys
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import components.csv_clean as cc
from components.import_csv_std2 import location2


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#8E3DEB'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#

# df can be used to get all/any columns from original csv
df = pd.read_csv(location2)

# for mor specific values use the methods/functions created in csv_clean
current_holdings = cc.cumsum_current_holdings(location2)



line = px.line(current_holdings, x="Date", y="Holdings", title='Current holdings')
bar = px.bar(df, x="Date", y=["Credit","Debit"], color="Remark", barmode="group")
pie = px.pie(df, values="Credit", names="Remark", title="All Bonuses")

'''
bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
),

pie.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
),
'''


layout = html.Div(style={'backgroundColor': colors['background']}, 
children=   
    [
        dcc.Graph(
            id='example-graph-2',
            figure=line
        ),

        dcc.Graph(
            id='example-graph-2',
            figure=bar
        ),

        dcc.Graph(
            id='example-graph-3',
            figure=pie
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)