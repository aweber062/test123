import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("formatted_output.csv")

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualization"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin": "10px"},
        ),
        dcc.Graph(id="sales-chart"),
    ]
)
@app.callback(
    dash.dependencies.Output("sales-chart", "figure"),
    [dash.dependencies.Input("region-filter", "value")]
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
        
    figure = {
        "data": [
            {
                "x": filtered_df["date"],
                "y": filtered_df["sales"],
                "type": "line",
                "name": "Sales",
            }
        ],
        "layout": {
            "title": "Sales Over Time",
            "xaxis": {"title": "Date"},
            "yaxis": {"title": "Sales"},
        },
    }
    
    return figure

app.css.append_css(
    {
        "external_url": "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)