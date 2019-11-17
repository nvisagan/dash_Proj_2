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
            # Process
            ---
            ### Introduction
            Most deaths are issued a death certificate detailing the specifics of the person and the cause of death. 
            In rare cases, the certificate may not have the person’s name and classify him as a John or Jane Doe. 
            In extreme cases, the gender of the deceased cannot be specified due to various obstacles. 
            I wondered in such scenarios is it possible to guess the gender based on various circumstances. Let's take a look.

            ### Dataset
            This [dataset](https://catalog.data.gov/dataset/new-york-city-leading-causes-of-death-ce97f) consists of leading causes of death by sex and ethnicity in New York City since 2007. The dataset contains 1380 rows. A few of the features are explained in the predictions tab, but for more clarification:
            * **Year**: The year of death
            * **Leading Cause**: The cause of death
            * **Sex**: The deceased’s sex
            * **Race Ethnicity**: The deceased ethnicity
            * **Deaths**: The number of people who died due to cause of death 
            * **Death Rate** The death rate within the sex and race/ethnicity category
            * **Age-Adjusted Death Rate**: The age-adjusted death rate within the sex and race/ethnicity category

            ### Cleaning
            Most datasets need to be cleaned properly. This one was no exception. Luckily, it wasn't too strenuous. The first order of business was to clean the NaN values. 
            I had the idea of filling the NaN's with the means of the columns. However, the columns were not numeric. I simply changed them with `pd.to_numeric` and filled the NaN
            values using `df['column'].fillna((df['column'].mean()), inplace=True)`. Another small cleanup I preformed was making sure the sex column had the same string values throughout.
            The earlier portion of the data had recorded male and female as *M* and *F*. Using the `.replace` function *M* became Male and *F* became Female for consistency.

            ### Modeling
            I had chosen predict sex of deceased. In this case, my target was a binary classification problem (Male or Female). My baseline was 50.5435. To be this score, I used a random forest classifier.
            ```python
            pipeline = make_pipeline(
            ce.OrdinalEncoder(), 
            SimpleImputer(strategy='median'), 
            RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=42)
            )
            pipeline.fit(X_train, y_train);
            ``` 
            This gave me an accuracy score of 71.015

            ### Conclusion & What's next
            This was an interesting project. Each step of the process I was learning and reinforcing various skills I learned of the past two units. I want to come back and try a multi-classification problem,
            with my target as the Leading Cause of death. I feel it could more useful to predict how a person died than simplying predicting the gender of the deceased. Of course, the HTML components can be cleaned up also.
            But all of that is for another time. The github repo is linked below as well as my various social outlets so you can follow my data science and machine learning journey. 
                
            """
        ),

    ],
)

layout = dbc.Row([column1])
