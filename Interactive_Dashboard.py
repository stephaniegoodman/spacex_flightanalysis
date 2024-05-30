# required libraries
import pandas as pd
import dash
import dash_html_componenets as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# read airline data into pd dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = space_df['Payload Mass (kg)'].min()

# create dash application
app = dash.Dash(__name__)

# create app layoud
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # Task 1: add dropdown list to select Launch Site
                                # Default value: all sites
                                dcc.Dropdown(id='site-dropdown',
                                  options=[
                                    {'label': 'All Sites', 'value': 'ALL'},
                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'

                                  ],
                                  value='ALL',
                                  placeholder="Select Launch Site",
                                  searchable=True
                                  ),
                                html.Br(),

                                # Task 2: add pie chart to show total count of successful launches for all sites
                                # if specific launch site is selected, show success vs failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # Task 3: Add slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                                                value=[min_payload, max_payload]),
                                # Task 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                               ])
# Task 2:
# Add callback function for 'site-dropdown' as input, 'success-pie-chart as output
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
  filtered_df = spacex_df
  if entered_site == 'ALL':
    fig = px.pie(filtered_df, values='class',
    names='Launch Site',
    title='Total Success Launches by Site')
    return fig
  else: 
    # return outcomes piechart for specified site
    filtered_df = spacex_df[space_df['Launch Site'] == entered_site],
    x = 'Payload Mass (kg)', y='class',
    color = 'Booster Version Category',
    title=f'Correlation between Payload and Sucess for Site {entered_site}')
    return fig 

# Run app
if __name__ == '__main__':
  app.run_server()

