import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import last_update as lu

covid_map_3d = px.scatter_geo(
    lu.global_Confirmed,
    lat="Lat",
    lon="Long",
    projection="orthographic",
    color="Country/Region",
    opacity=.8,
    hover_data=[lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
                lu.global_Confirmed[lu.global_Confirmed.columns[-1]] - lu.global_Confirmed[lu.global_Confirmed.columns[-2]]],
    hover_name="Province/State",
    height=600,
    template="plotly_dark"
)
covid_map_3d.update_layout(margin=dict(l=60, r=60, t=50, b=50))

covid_map_2d = px.scatter_mapbox(
    lu.global_Confirmed,
    lat="Lat",
    lon="Long",
    color="Country/Region",
    hover_data=[lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
                lu.global_Confirmed[lu.global_Confirmed.columns[-1]] - lu.global_Confirmed[lu.global_Confirmed.columns[-2]]],
    hover_name="Province/State",
    height=600,
    zoom=1,
    template="plotly_dark"
)
covid_map_2d.update_layout(mapbox_style="open-street-map")
covid_map_2d.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
covid_plot = px.bar(
    lu.global_Confirmed,
    x="Country/Region",
    y=lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
    color="Country/Region",
    template="plotly_dark",
    height=800,
    animation_frame=lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
    animation_group="Country/Region",
)
data = {
    "Case": [lu.total_vaccines_poland, lu.people_vaccines_poland, lu.people_fully_poland],
    "Label": ["Total vaccines", "1 vaccine dose", "2 vaccine dose"],
}
df = pd.DataFrame(data, columns=["Case", "Label"])
covid_vc_pl = px.pie(
    df,
    values="Case",
    names="Label",
    color="Label",
    color_discrete_map={
        "Total vaccines": "#41b1e0",
        "1 vaccine dose": "#307fa1",
        "2 vaccine dose": "#3b6d82"
    },
    height=500,
    width=416,
    template="plotly_dark",
)
covid_vc_pl.update_layout({"paper_bgcolor": "#1b1c1c"})
data = {
    "Case": [lu.daily_poland_confirmed, lu.daily_poland_deaths, lu.daily_poland_recovered],
    "Label": ["Daily confirmed", "Daily deaths", "Daily recovered"]
}
df = pd.DataFrame(data, columns=["Case", "Label"])
covid_bar_plot = px.bar(
    df,
    x="Label",
    y="Case",
    color="Label",
    height=420,
    width=416,
    template="plotly_dark",
)
covid_bar_plot.update_layout({"paper_bgcolor": "#1b1c1c"})
data = {
    "Case": [13125, lu.count_test],
    "Label": ["People hospitalized", "Number of Tests"]
}
df = pd.DataFrame(data, columns=["Case", "Label"])
covid_bubble_char = px.scatter(
    df,
    x="Label",
    y="Case",
    size="Case",
    color="Label",
    height=420,
    width=416,
    template="plotly_dark",
)
covid_bubble_char.update_layout({"paper_bgcolor": "#1b1c1c"})
external_stylesheets = [
    {
        "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css",  # Bootstrap css
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "Dashboard Coronavirus"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children="Dashboard Covid-19", className="header-title"
                ),
                html.P(
                    children="Analysis of data from the world and Poland on the COVID19",
                    className="header-description",
                ),
            ], className="header",
        ),


        html.Div(
            [
                html.Div(children=[html.H1("Global Cases", style={
                    "font-size": "15px",
                    "margin-top": "10px",
                    "color": '#ffb62e',
                }), html.P(f"{lu.gc:,.0f}")], style={
                    "font-size": "30px",
                    "color": 'white',
                    "width": "430px",
                    "height": "100px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                }),
                html.Div(children=[html.H1("Global Death", style={
                    "font-size": "15px",
                    "margin-top": "10px",
                    "color": '#f060e1',
                }), html.P(f"{lu.gd:,.0f}")], style={
                    "font-size": "30px",
                    "color": 'white',
                    "width": "430px",
                    "height": "100px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                }),
                html.Div(children=[html.H1("Global Recovered", style={
                    "font-size": "15px",
                    "margin-top": "10px",
                    "color": '#23cfdb',
                }), html.P(f"{lu.gr:,.0f}")], style={
                    "font-size": "30px",
                    "color": 'white',
                    "width": "430px",
                    "height": "100px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                })
            ], className="container", style={"text-align": "center"}),


        html.Div([

                html.Div(children=[html.H1("Total Vaccines", style={
                    "font-size": "13px",
                    "margin-top": "10px",
                    "color": 'white',
                }), html.P(f"{lu.gv:,.0f}")], style={
                    "font-size": "20px",
                    "color": 'white',
                    "width": "430px",
                    "height": "70px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                }),

                html.Div(children=[html.H1("People Vaccined", style={
                    "font-size": "13px",
                    "margin-top": "10px",
                    "color": 'white',
                }), html.P(f"{lu.gv_people:,.0f}")], style={
                    "font-size": "20px",
                    "color": 'white',
                    "width": "430px",
                    "height": "70px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                }),

                html.Div(children=[html.H1("People Fully Vaccined", style={
                    "font-size": "13px",
                    "margin-top": "10px",
                    "color": 'white',
                }), html.P(f"{lu.gv_people_full:,.0f}")], style={
                    "font-size": "20px",
                    "color": 'white',
                    "width": "430px",
                    "height": "70px",
                    "margin-top": "20px",
                    "text-align": "center",
                    "display": "inline-block",
                    "border-style": "solid",
                    "border-width": "1px",
                    "border-color": "gray",
                    "background-color": "#222222",
                }),

        ],className="container", style={"text-align": "center"}),


            html.Br(),
            html.Div(children=html.Div([
                html.Div([
                    html.H4(f"Last update: {lu.date_poland_vaccines}", style={"color": "white"}),
                    dcc.Graph(figure=covid_vc_pl),
                ], className="col"),
                html.Div([
                    html.H4(f"Last update: {lu.tests_Date}", style={"color": "white"}),
                    dcc.Graph(figure=covid_bubble_char),
                ], className="col"),
                html.Div([
                    html.H4(f"Last update: {lu.last_day}", style={"color": "white"}),
                    dcc.Graph(figure=covid_bar_plot),
                ], className="col"),
            ], className="row"), className="container"),

            html.Div([
                dcc.Dropdown(id="input_state", options=[
                    {"label": "Total Cases", "value": "Total"},
                    {"label": "Total Deaths", "value": "Deaths"},
                    {"label": "Total Recovered", "value": "Recovered"},
                ], className="container", value="Total"),
                html.Div(id="output_state"),
            ], style={"text-align": "center"}),

            html.Br(),
            html.Div(id="plotDiv", children=dcc.Graph(id="plot", figure=covid_plot), className="container"),
            html.Br(),
            html.Div([
                dcc.Dropdown(id="input_view", options=[
                    {"label": "2D VIEW", "value": "2D"},
                    {"label": "3D VIEW", "value": "3D"},
                    ], className="container", value="3D"),
                    html.Div(id="output_view"),
                ], style={"text-align": "center"}
            ),
            html.Br(),
            html.Div(id="3d_map", children=dcc.Graph(id="map_view", figure=covid_map_3d), className="container"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),


    ],
)

@app.callback(
    [Output("output_view", "children"), Output(component_id="map_view", component_property="figure")],
    [Input(component_id="input_view", component_property="value")]
)
def update_map_view(type_of_view):
    if type_of_view is None:
        raise PreventUpdate
    else:
        map_ = None
        if type_of_view == "2D":
            map_ = px.scatter_mapbox(
                lu.global_Confirmed,
                lat="Lat",
                lon="Long",
                color="Country/Region",
                hover_data=[lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
                            lu.global_Confirmed[lu.global_Confirmed.columns[-1]] - lu.global_Confirmed[
                                lu.global_Confirmed.columns[-2]]],
                hover_name="Province/State",
                height=600,
                zoom=1,
                template="plotly_dark"
            )
            map_.update_layout(mapbox_style="open-street-map")
            map_.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        elif type_of_view == "3D":
            map_ = px.scatter_geo(
                lu.global_Confirmed,
                lat="Lat",
                lon="Long",
                projection="orthographic",
                color="Country/Region",
                opacity=.8,
                hover_data=[lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
                            lu.global_Confirmed[lu.global_Confirmed.columns[-1]] - lu.global_Confirmed[
                                lu.global_Confirmed.columns[-2]]],
                hover_name="Province/State",
                height=600,
                template="plotly_dark"
            )
            map_.update_layout(margin=dict(l=60, r=60, t=50, b=50))
        return "View: " + type_of_view, map_

@app.callback(
    [Output("output_state", "children"), Output(component_id="plot", component_property="figure")],
    [Input(component_id="input_state", component_property="value")]
)
def update_covid_plot(data_type):
    if data_type is None:
        raise PreventUpdate
    else:
        covid_plot = None
        if data_type == "Total":
            covid_plot = px.bar(
                lu.global_Confirmed,
                x="Country/Region",
                y=lu.global_Confirmed[lu.global_Confirmed.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        elif data_type == "Deaths":
            covid_plot = px.bar(
                lu.global_Deaths,
                x="Country/Region",
                y=lu.global_Deaths[lu.global_Deaths.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        elif data_type == "Recovered":
            covid_plot = px.bar(
                lu.global_Recovered,
                x="Country/Region",
                y=lu.global_Recovered[lu.global_Recovered.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        return "Category: " + data_type, covid_plot

if __name__ == "__main__":
    app.run_server(debug=True)
