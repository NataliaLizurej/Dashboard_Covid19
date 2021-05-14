import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

global_Confirmed = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
global_Recovered = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv")
global_Deaths = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")

#Global Cases:
gc = global_Confirmed[global_Confirmed.columns[-1]].sum()
#Global Recovered:
gr = global_Recovered[global_Recovered.columns[-1]].sum()
#Global Deaths:
gd = global_Deaths[global_Deaths.columns[-1]].sum()


# external_stylesheets = [
#     {
#         "href": "https://fonts.googleapis.com/css2?"
#         "family=Lato:wght@400;700&display=swap",
#         "rel": "stylesheet",
#     },
# ]


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

                # html.Div([
                #     html.P(children="LEWA KOLUMNA", style={
                #         "color": "white",
                #         "border": "solid 1px #FFFFFF",
                #         "float": "left",
                #         "height": "300px",
                #         "width": "300px",
                #         "margin-top": "20px",
                #         "margin-right": "0.5%",
                #     })
                # ], className="leftColumn"),

                html.Div([
                    html.H6(children='LEWA KOLUMNA',
                            style={
                                'margin-top': '15px',
                                'text-align': 'center',
                                'color': 'white'
                            },
                            ),
                    html.P(children=0, style={
                        'color': 'green'
                    }),


                ], className='columns'),

                html.Div([
                    html.H6(children='Global Cases',
                            style={
                                'margin-top': '15px',
                                'text-align': 'center',
                                'color': 'white'
                            },
                            ),
                    html.P(children=1, style={
                        'color': 'white'
                    })
                ], className='three-columns1'),

                html.Div([
                    html.H6(children='Death Cases',
                            style={
                                'margin-top': '15px',
                                'text-align': 'center',
                                'color': 'white'
                            },
                            ),
                    html.P(children=0, style={
                        'color': 'red'

                    })
                ], className='three-columns1'),

                html.Div([
                    html.H6(children='Death Recovered',
                            style={
                                'margin-top': '15px',
                                'text-align': 'center',
                                'color': 'white'
                            },
                            ),
                    html.P(children=0, style={
                        'color': 'green'
                    })
                ], className='three-columns1'),

                html.Div([
                    html.H6(children='PRAWA KOLUMNA',
                            style={
                                'margin-top': '15px',
                                'text-align': 'center',
                                'color': 'white'
                            },
                            ),
                    html.P(children=0, style={
                        'color': 'green'
                    })
                ], className='columns'),



                # PLOT
                html.Div(children=dcc.Graph(
                        figure={
                            "data": [
                                {
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": "Plot",
                            },
                        },
                ), style={
                    "width": "66%",
                    "margin-left": "15.9%",
                    "margin-top": "-24%",
                })



            ],
            style={
                "margin-left": "2%",
            }
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
