import pandas as pd
import dash
from dash import dcc
from dash import html
import os

os.chdir('../../Users/andre.DESKTOP-DFG3GU2/Documents/GitHub/figshare-api-scripts/reporting')

#df_final = pd.read_csv("dfFinal.csv")
top_cats = pd.read_csv("topCats.csv")
funder_view_count = pd.read_csv("funderViews.csv")

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Statistics from Batch Downloaded Metadata",),
        html.P(
            children="Display basic charts based on metadata",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": top_cats["category"],
                        "y": top_cats["count"],
                        "type": "bars",
                    },
                ],
                "layout": {"title": "Top 10 Categories"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": funder_view_count["funder_name"],
                        "y": funder_view_count["views"],
                        "type": "bars",
                    },
                ],
                "layout": {"title": "Views by Funder"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=False)