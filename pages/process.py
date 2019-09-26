import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process

            ### Introduction
            I wanted to create a predictive model surrounding the health of people. I looked at various
            datasets on different repositories and collections pertaining to health. Originally I looked at E-coli outbreaks, but this did not excite me
            I  


            """
        ),

    ],
)

layout = dbc.Row([column1])