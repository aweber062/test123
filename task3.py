import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("formatted_output.csv")
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualization"),
        dcc.Graph(
            id="sales-chart",
            figure={
                "data": [
                    {
                        "x": df["date"],
                        "y": df["sales"],
                        "type": "line",
                        "name": "Sales",
                    }
                ],
                "layout": {
                    "title": "Sales Over Time",
                    "xaxis": {"title": "Date"},
                    "yaxis": {"title": "Sales"},
                },
            },
        ),
    ]
)
if __name__ == "__main__":
    app.run_server(debug=True)