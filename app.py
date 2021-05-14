import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import numpy as np

# Github links

global_Confirmed = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
global_Recovered = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
global_Deaths = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
global_Vaccinations = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")

#Pandas
#Global Cases:
gc = global_Confirmed[global_Confirmed.columns[-1]].sum()
#Global Recovered:
gr = global_Recovered[global_Recovered.columns[-1]].sum()
#Global Deaths:
gd = global_Deaths[global_Deaths.columns[-1]].sum()
#Vaccinations:
u = global_Vaccinations.index[-1] #ostatni indeks
z = global_Vaccinations['date'].loc[u] #ostatnia data
#Total Vaccinations
gv = global_Vaccinations[global_Vaccinations.columns[3]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#People vaccinated
gv_people = global_Vaccinations[global_Vaccinations.columns[4]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#People fully vaccinated
gv_people_full = global_Vaccinations[global_Vaccinations.columns[5]][(global_Vaccinations['location'] == 'World') & (global_Vaccinations['date'] == z)].sum()
#Number of Country/Regions:
g_country_regions = global_Confirmed['Country/Region'].nunique() # jest 192


#######################################

covid_map_3d = px.scatter_geo(
    global_Confirmed,
    lat="Lat",
    lon="Long",
    projection="orthographic",
    color="Country/Region",
    opacity=.8,
    hover_data=[global_Confirmed[global_Confirmed.columns[-1]],
                global_Confirmed[global_Confirmed.columns[-1]] - global_Confirmed[global_Confirmed.columns[-2]]],
    hover_name="Province/State",
    height=600,
    template="plotly_dark"
)
covid_map_3d.update_layout(margin=dict(l=60, r=60, t=50, b=50))
#######################################
covid_map_2d = px.scatter_mapbox(
    global_Confirmed,
    lat="Lat",
    lon="Long",
    color="Country/Region",
    hover_data=[global_Confirmed[global_Confirmed.columns[-1]],
                global_Confirmed[global_Confirmed.columns[-1]] - global_Confirmed[global_Confirmed.columns[-2]]],
    hover_name="Province/State",
    height=600,
    zoom=1,
    template="plotly_dark"
)
covid_map_2d.update_layout(mapbox_style="open-street-map")
covid_map_2d.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
#######################################
covid_plot = px.bar(
    global_Confirmed,
    x="Country/Region",
    y=global_Confirmed[global_Confirmed.columns[-1]],
    color="Country/Region",
    template="plotly_dark",
    height=800,
    animation_frame=global_Confirmed[global_Confirmed.columns[-1]],
    animation_group="Country/Region",
)
#######################################

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
                    "color": 'white',
                }), html.P(f"{gc:,.0f}")], style={
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
                    "color": 'white',
                }), html.P(f"{gd:,.0f}")], style={
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
                    "color": 'white',
                }), html.P(f"{gr:,.0f}")], style={
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

        ]),


            html.Br(),
            ###############################################################################################
            html.Div([
                # dcc.Input(id="input_state", type="text", value="Total", required=True),
                dcc.Dropdown(id="input_state", options=[
                    {"label": "Total Cases", "value": "Total"},
                    {"label": "Total Deaths", "value": "Deaths"},
                    {"label": "Total Recovered", "value": "Recovered"},
                ], className="container", value="Total"),
                html.Div(id="output_state"),
            ], style={"text-align": "center"}),
            ###############################################################################################
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
            # html.Div(id="2d_map", children=dcc.Graph(figure=covid_map_2d), className="container"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),


    ],
)
#########################################################################################################
# dataset_copy = global_Confirmed
# dataset_copy = dataset_copy.drop(columns=["Lat", "Long", "Province/State"])
# dataset_copy = dataset_copy.groupby(by="Country/Region").aggregate(np.sum).T
# dataset_copy.index.name = "Date"
# dataset_copy = dataset_copy.reset_index()
#########################################################################################################
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
                global_Confirmed,
                lat="Lat",
                lon="Long",
                color="Country/Region",
                hover_data=[global_Confirmed[global_Confirmed.columns[-1]],
                            global_Confirmed[global_Confirmed.columns[-1]] - global_Confirmed[
                                global_Confirmed.columns[-2]]],
                hover_name="Province/State",
                height=600,
                zoom=1,
                template="plotly_dark"
            )
            map_.update_layout(mapbox_style="open-street-map")
            map_.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        elif type_of_view == "3D":
            map_ = px.scatter_geo(
                global_Confirmed,
                lat="Lat",
                lon="Long",
                projection="orthographic",
                color="Country/Region",
                opacity=.8,
                hover_data=[global_Confirmed[global_Confirmed.columns[-1]],
                            global_Confirmed[global_Confirmed.columns[-1]] - global_Confirmed[
                                global_Confirmed.columns[-2]]],
                hover_name="Province/State",
                height=600,
                template="plotly_dark"
            )
            map_.update_layout(margin=dict(l=60, r=60, t=50, b=50))
        return "View: " + type_of_view, map_
#########################################################################################################
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
                global_Confirmed,
                x="Country/Region",
                y=global_Confirmed[global_Confirmed.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        elif data_type == "Deaths":
            covid_plot = px.bar(
                global_Deaths,
                x="Country/Region",
                y=global_Deaths[global_Deaths.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        elif data_type == "Recovered":
            covid_plot = px.bar(
                global_Recovered,
                x="Country/Region",
                y=global_Recovered[global_Recovered.columns[-1]],
                color="Country/Region",
                template="plotly_dark",
                height=800,
            )
        return "Category: " + data_type, covid_plot
#########################################################################################################




if __name__ == "__main__":
    app.run_server(debug=True)
