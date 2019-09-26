import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline.joblib')

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## John or Jane Doe 
            Use the interactive menus to create different scenarios to predict the gender of the deceased


            """
        ), 
        dcc.Markdown('#### Year'), 
        dcc.Slider(
            id='Year', 
            min=2007, 
            max=2016, 
            step=1, 
            value=2010, 
            marks={n: str(n) for n in range(2007,2017)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Race/Ethnicity'), 
        dcc.Dropdown(
            id='Race/Ethnicity', 
            options = [
                {'label': 'Other Race/ Ethnicity', 'value': 'Other Race/ Ethnicity'}, 
                {'label': 'Non-Hispanic White', 'value': 'Non-Hispanic White'}, 
                {'label': 'Asian and Pacific Islander', 'value': 'Asian and Pacific Islander'}, 
                {'label': 'Hispanic', 'value': 'Hispanic'}, 
                {'label': 'Not Stated/Unknown', 'value': 'Not Stated/Unknown'},
                {'label': 'Non-Hispanic Black', 'value': 'Non-Hispanic Black'},
                {'label': 'Black Non-Hispanic', 'value': 'Black Non-Hispanic'},
                {'label': 'White Non-Hispanic', 'value': 'White Non-Hispanic'}
            ], 
            value = 'Africa', 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Lifespan', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)


layout = dbc.Row([column1, column2])