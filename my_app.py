import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Data Visualizer"),
        dcc.Graph(
            id="sales-chart",
            figure={
                "data": [
                    {"x": [1, 2, 3, 4], "y": [4, 1, 3, 5], "type": "bar", "name": "Sales"}
                ],
                "layout": {"title": "Sales Data"},
            },
        ),
        html.Div(
            [
                html.Label("Region Picker"),
                dcc.RadioItems(
                    id="region-picker",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="north",
                ),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
