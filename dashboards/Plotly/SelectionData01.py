import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
import base64

app = dash.Dash()

np.random.seed(42)

x1=np.linspace(0.1,5,50)
x2=np.linspace(5.1,10,50)
y= np.random.randint(0,50,50)


#DFs
df1= pd.DataFrame({'x':x1,'y':y})
df2= pd.DataFrame({'x':x1,'y':y})
df3= pd.DataFrame({'x':x2,'y':y})

df = pd.concat([df1,df2,df3],ignore_index=True)


app.layout = html.Div([
    dcc.Graph(id='plot',
              figure={'data':go.Scatter(
                  x=df['x'],
                  y=df['y'],
                  mode='markers'
              )})
])
