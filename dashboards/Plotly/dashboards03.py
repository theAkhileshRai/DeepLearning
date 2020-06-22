import dash
import dash_core_components as doc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
app = dash.Dash()

np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y =  np.random.randint(1,101,100)

app.layout = html.Div(children = [html.H1('Hello Dash!'),
                                  html.Div('Dash: Web Dashboards with Python'),
                                  doc.Graph(id= 'Scatter',figure={'data': [go.Scatter(x=random_x,y=random_y,mode='markers',
                                                                                        marker = {
                                                                                            'size': 12,
                                                                                            'color':'rgb(51,204,153)',
                                                                                            'symbol':'pentagon'
                                                                                            }
                                                                                      )],
                                                                  'layout': {'title':'Scatter',
                                                                             'axis':{'title':'Some X Title'}
                                                                             }})])

if __name__ == '__main__':
  app.run_server(debug=True)
