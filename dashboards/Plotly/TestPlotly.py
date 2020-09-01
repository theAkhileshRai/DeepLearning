import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv("mpg.csv",delimiter=",")
print(df.head())

app = dash.Dash()

app.layout= html.Div([
                dcc.Graph(id="mpg-scatter",
                          figure={
                              'data':[go.Scatter(
                                        x= df['model_year']+1900,
                                        y= df['mpg'],
                                        text=df['name'],
                                        hoverinfo= 'text+y',
                                        mode = 'markers'
                              )],
                              'layout':go.Layout(title='MPG Data',
                                                 xaxis={'title':'Model year'},
                                                 yaxis={'title':'MPG'},
                                                 hovermode='closest')
                          })
])

if __name__ == '__main__':
    app.run_server()
