import dash 
#import dash_core_components as dcc
from dash import dcc
from dash.dash import Dash
import dash_html_components as html
#from dash_html_components.Div import Div
from numpy.lib.arraypad import pad
import plotly.graph_objects as go
import plotly.express as px
import dash_table
import pandas as pd 
import colorlover as cl
from dash.dependencies import Input, Output
import numpy as np
import csv
import dash_auth
from dash import dash_table
from dash import html
import dash_table.FormatTemplate as FormatTemplate



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

VALID_USERNAME_PASSWORD_PAIRS = {
    ' ': ' '
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "BAT TECH DASHBOARD"
server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

df = pd.read_csv('mood_drivers_app.csv')
df = df.mood

def build_banner():
    return dcc.Markdown('''
    ### *Butterfly.ai Visualization Dashboard* 
        ''')

def build_bannar1():
     return dcc.Markdown('''
    *** 1. ***please select your desired ***Mood Driver***.
         ''')

def build_intro():
    return dcc.Markdown('''
    Welcome to the BAT Tech visualization app!
    ''')

def build_bannar2():
     return dcc.Markdown('''
    *** Where Mood =***.
         ''')



def build_dropdown():

    return html.Div([
        dcc.Dropdown(
        id = 'dropdown',
        options=[
        {'label': 'Feedback', 'value': 'feedback'},
        {'label': 'Colleagues', 'value': 'colleagues',},
        {'label': 'Growth', 'value': 'growth'},
        {'label': 'Career Path', 'value': 'career-path'},
        {'label': 'Transparency', 'value': 'transparency'},
        {'label': 'Well Being', 'value': 'well-being'},
        {'label': 'Autonomy', 'value': 'autonomy'},
        {'label': 'Determination', 'value': 'determination'},
        {'label': 'Motivation', 'value': 'motivation'},
        {'label': 'Agility', 'value': 'agility'},
        {'label': 'Respect', 'value': 'respect'},
        {'label': 'Accountability', 'value': 'accountability'},
        {'label': 'Role', 'value': 'role'},
        {'label': 'Management', 'value': 'management'},
        {'label': 'Recognition', 'value': 'recognition'},
        {'label': 'Workload', 'value': 'workload'},
        {'label': 'Collaboration', 'value': 'collaboration'},
        {'label': 'Support', 'value': 'support'},
        {'label': 'Curiosity', 'value': 'curiosity'},
        {'label': 'Impact', 'value': 'impact'},
        {'label': 'Empathy', 'value': 'empathy'},
        {'label': 'Resilience', 'value': 'resilience'},
        {'label': 'Happiness', 'value': 'happiness'},
        {'label': 'Training', 'value': 'training'},
        {'label': 'Life Satisfaction', 'value': 'life-satisfaction'},
        {'label': 'Balance', 'value': 'balance'},
        {'label': 'Environment', 'value': 'environment'},
        {'label': 'Accomplishment', 'value': 'accomplishment'},
        {'label': 'Alignment', 'value': 'alignment'},
        {'label': 'Inclusion', 'value': 'inclusion'},
        {'label': 'Confidence', 'value': 'confidence'},
        {'label': 'Courage', 'value': 'courage'},
        {'label': 'Productivity', 'value': 'productivity'},
        {'label': 'Acknowledgment', 'value': 'acknowledgment'},
        {'label': 'Sabotage', 'value': 'sabotage'},
        {'label': 'Reward', 'value': 'reward'},
        {'label': 'Safety', 'value': 'safety'}
        ],
        value="val")])

 
def build_button():
    return html.Button(
        'GO', id = 'button')


def build_mood_select():

    return html.Div([
        dcc.Dropdown(
        id='mood_dropdown',
        options=[
            {'label': '1', 'value': '1'},
            {'label': '2', 'value': '2'},
            {'label': '3', 'value': '3'},
            {'label': '4', 'value': '4'},
            {'label': '5', 'value': '5'},
            {'label': 'None', 'value': 'None'}
        ],
        value='val')
     ]
     )

def build_plot():

    fig = px.histogram(df, x = 'mood')

    return dcc.Graph(id = 'plot_output', figure = fig)


app.layout = html.Div(
    #id = 'body',
    style={
        'margin-left': 80,
        'margin-right': 80,
        'margin-top': 80,
        'margin-bottom': 80
    },
    id="body",
    children=[

        html.Div(
            build_banner(),
        ),

        dcc.Tabs([
        dcc.Tab(label='Home', children=[

            build_intro()

        ]),
        dcc.Tab(label='Distribution Generator', children=[
            build_bannar1(),
            build_dropdown(),
            build_bannar2(),
            html.Div([build_mood_select(), build_button()]),
            html.Div(id='dd-output-container'),

            html.Div(build_plot())
        ]
        )

        ]
        )
    ])

@app.callback(dash.dependencies.Output('plot_output', 'figure'),
[dash.dependencies.Input('dropdown', 'value'),
dash.dependencies.Input('mood_dropdown', 'value'),
dash.dependencies.Input('button', 'n_clicks')])

def update_charts(dropdown_value, mood_dropdown_value, n_clicks):

    print(dropdown_value)
    if not n_clicks:
        df = pd.read_csv('mood_drivers_app.csv', index_col=None)[['mood']+[dropdown_value]]
        #print(df)
        #df = df.groupby([dropdown_value])['count'].sum().reset_index()
        if mood_dropdown_value != 'None':
            df = df.groupby('mood').get_group(int(mood_dropdown_value))
        fig = px.histogram(df, x=dropdown_value, title = 'Distribution of Selected Driver', color_discrete_sequence=['rgb(111,227,206)'])
        fig.update_layout(bargap=0.2)

        return fig.show()
    



if __name__ == '__main__':
    app.run_server(debug=True)