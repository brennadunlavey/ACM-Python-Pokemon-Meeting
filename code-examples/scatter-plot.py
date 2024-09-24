# make a scatter plot of peoples age vs salary
# uses pandas and plotly to open the scatter plot in a web browser

import pandas as pd
import plotly.express as px

myObj = [
    {'name': 'Alice', 'age': 25, 'salary': 55000},
    {'name': 'Bob', 'age': 43, 'salary': 120000},
    {'name': 'Craig', 'age': 19, 'salary': 30000},
    {'name': 'Daphne', 'age': 39, 'salary': 70000},
    {'name': 'Edward', 'age': 51, 'salary': 95300},
    {'name': 'Fred', 'age': 23, 'salary': 35750},
    {'name': 'Gertrude', 'age': 31, 'salary': 105350},
    {'name': 'Harry', 'age': 46, 'salary': 150500},
    {'name': 'Isabel', 'age': 39, 'salary': 51400},
    {'name': 'Justin', 'age': 55, 'salary': 120100},
    {'name': 'Kaden', 'age': 21, 'salary': 95000}
]



df = pd.DataFrame(myObj)

fig = px.scatter(df,'age','salary', hover_name='name')
fig.show()
