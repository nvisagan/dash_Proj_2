import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

row1 = dbc.Row(
    [
        dcc.Markdown(
            """
        
            ## Insights
            I wanted to create a predictive model surrounding the health of people. I looked at various
            datasets on different repositories and collections pertaining to health. Originally I looked at E-coli outbreaks, but that wasn't as exciting as it seemed.
            Looking through datasets on HealthData.gov, I found a dataset on the leading cause of death in New York since 2007.

            """
        ),
        

    ],
)

row2 = html.Div([
    html.H1('Feature Importances'),
    html.Div([
        html.P('Heres a look at the feature importances'),
        html.Img(src='assets/plot.png', className='img-fluid')
    ])
])

row3 = html.Div([
    html.H1('Permutation Importance'),
    html.Div([
        html.P('Heres a look at the permutation importance'),
        html.Img(src='assets/Permutaion Importance.PNG', className='img-fluid')
    ])
])




layout = dbc.Row([row1,row2,row3])