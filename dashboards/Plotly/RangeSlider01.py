import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
# import base64

app = dash.Dash()
app.layout = html.Div(
                [dcc.RangeSlider(id = 'range-slider',
                           min=-10,
                           max = 10,
                           step = 1,
                           marks={i:str(i) for i in range(-10,11)},
                           value=[-10,10]),
                html.H1(id='product')])
@app.callback(Output('product','children'),[Input('range-slider','value')])
def Slider(value_list):
    return value_list[0]*value_list[1]

if __name__ == '__main__':
    app.run_server(debug=True)
