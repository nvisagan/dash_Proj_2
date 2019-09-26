import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline.joblib')
import pandas as pd

from app import app



column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            # John or Jane Doe 
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
        dcc.Markdown('#### Race Ethnicity'), 
        dcc.Dropdown(
            id='Race Ethnicity', 
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
            value = 'Hispanic', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Cause of Death'), 
        dcc.Dropdown(
            id='Leading Cause', 
            options = [
                {'label': 'Essential Hypertension and Renal Diseases', 'value': 'Essential Hypertension and Renal Diseases (I10, I12)'}, 
                {'label': 'All Other Causes', 'value': 'All Other Causes'}, 
                {'label': 'Accidents Except Drug Poisoning', 'value': 'Accidents Except Drug Poisoning (V01-X39, X43, X45-X59, Y85-Y86)'}, 
                {'label': 'Intentional Self-Harm/Suicide', 'value': 'Intentional Self-Harm (Suicide: U03, X60-X84, Y87.0)'}, 
                {'label': 'Diabetes Mellitus', 'value': 'Diabetes Mellitus (E10-E14)'},
                {'label': "Alzheimer's Disease", 'value': "Alzheimer's Disease (G30)"},
                {'label': 'Cerebrovascular Disease', 'value': 'Cerebrovascular Disease (Stroke: I60-I69)'},
                {'label': 'Influenza (Flu) and Pneumonia', 'value': 'Influenza (Flu) and Pneumonia (J09-J18)'},
                {'label': 'Chronic Lower Respiratory Diseases', 'value': 'Chronic Lower Respiratory Diseases (J40-J47)'},
                {'label': 'Diseases of Heart', 'value': 'Diseases of Heart (I00-I09, I11, I13, I20-I51)'},
                {'label': 'Malignant Neoplasms', 'value': 'Malignant Neoplasms (Cancer: C00-C97)'},
                {'label': 'Mental and Behavioral Disorders due to Accidental Poisoning and Other Psychoactive Substance Use', 'value': 'Mental and Behavioral Disorders due to Accidental Poisoning and Other Psychoactive Substance Use (F11-F16, F18-F19, X40-X42, X44)'},
                {'label': 'Chronic Liver Disease and Cirrhosis', 'value': 'Chronic Liver Disease and Cirrhosis (K70, K73-K74)'},
                {'label': 'HIV', 'value': 'Human Immunodeficiency Virus Disease (HIV: B20-B24)'},
                {'label': 'Peptic Ulcer', 'value': 'Peptic Ulcer (K25-K28)'},
                {'label': 'Assault', 'value': 'Assault (Homicide: U01-U02, Y87.1, X85-Y09)'},
                {'label': 'Mental and Behavioral Disorders due to Use of Alcohol', 'value': 'Mental and Behavioral Disorders due to Use of Alcohol (F10)'},
                {'label': 'Congenital Malformations, Deformations, and Chromosomal Abnormalities', 'value': 'Congenital Malformations, Deformations, and Chromosomal Abnormalities (Q00-Q99)'},
                {'label': 'Viral Hepatitis', 'value': 'Viral Hepatitis (B15-B19)'},
                {'label': 'Certain Conditions originating in the Perinatal Period', 'value': 'Certain Conditions originating in the Perinatal Period (P00-P96)'},
                {'label': 'Nephritis, Nephrotic Syndrome and Nephrisis', 'value': 'Nephritis, Nephrotic Syndrome and Nephrisis (N00-N07, N17-N19, N25-N27)'},
                {'label': 'Septicemia', 'value': 'Septicemia (A40-A41)'},
                {'label': 'Assault/Homicide', 'value': 'Assault (Homicide: Y87.1, X85-Y09)'},
                {'label': 'Intentional Self-Harm', 'value': 'Intentional Self-Harm (Suicide: X60-X84, Y87.0)'},
                {'label': "Parkinson's Disease", 'value': "Parkinson's Disease (G20)"},
                {'label': 'Chronic Liver Disease and Cirrhosis', 'value': 'Chronic Liver Disease and Cirrhosis (K70, K73)'},
                {'label': 'Meningitis', 'value': 'Meningitis (G00, G03)'},
                {'label': 'Accidents Except Drug Posioning', 'value': 'Accidents Except Drug Posioning (V01-X39, X43, X45-X59, Y85-Y86)'},
                {'label': 'Aortic Aneurysm and Dissection', 'value': 'Aortic Aneurysm and Dissection (I71)'},
                {'label': 'Tuberculosis', 'value': 'Tuberculosis (A16-A19)'},
                {'label': 'Insitu or Benign / Uncertain Neoplasms', 'value': 'Insitu or Benign / Uncertain Neoplasms (D00-D48)'},
            ], 
            value = 'HIV', 
            className='mb-5',
        ),
    ],         
    md=4,
)


column2 = dbc.Col(
    [
        dcc.Markdown("""
            ### Deaths
                The number of people who died due to cause of death. 
            """), 
        dcc.Slider(
            id='Deaths', 
            min=5, 
            max=7050,
            step=10,  
            value=2416,
            marks={
             5: '5',
             1050: '1050',
             2050: '2050',
             3050: '3050',
             4050: '4050',
             5050: '5050',
             6050: '6050',
             7050: '7050'
            },
            className='mb-5',
        ),
         dcc.Markdown("""
        
            ### Death Rate
                The death rate within the sex and Race/ethnicity category 
            """), 
        dcc.Slider(
            id='Death Rate', 
            min=2.4, 
            max=491.4,
            step=1,  
            value=221.4,
            marks={
             0: '0',
             100: '100',
             200: '200',
             300: '300',
             400: '400',
             495: '495'
            },
            className='mb-5',
        ),
        dcc.Markdown("""
        
            ### Age Adjusted Death Rate
                The age-adjusted death rate within the sex and Race/ethnicity category 
            """), 
        dcc.Slider(
            id='Age Adjusted Death Rate', 
            min=2.5, 
            max=350.7,
            step=1,  
            value=149,
            marks={
             0: '0',
             100: '100',
             200: '200',
             300: '300',
             360: '360'
            },
            className='mb-5',
        ),
    ]
)




column3 = dbc.Col(
    [
        html.H2('Male or Female?', className='mb-5'), 
        html.Div(id='Sex', className='lead')
    ]
)


@app.callback(
    Output('Sex', 'children'),
    [Input('Year', 'value'), Input('Race Ethnicity', 'value'), Input('Leading Cause', 'value'), Input('Deaths', 'value'), Input('Death Rate', 'value'), Input('Age Adjusted Death Rate', 'value')],
)
def predict(Year, Race_Ethnicity,Leading_Cause,Deaths,Death_Rate,Age_Adjusted_Death_Rate):
    df = pd.DataFrame(
        columns=['Year', 'Race Ethnicity','Leading Cause','Deaths', 'Death Rate', 'Age Adjusted Death Rate'], 
        data=[[Year, Race_Ethnicity,Leading_Cause,Deaths,Death_Rate,Age_Adjusted_Death_Rate]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred}'


layout = dbc.Row([column1, column2, column3])