import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import base64
df = pd.read_csv('wheels.csv')

# print(df.head())

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app = dash.Dash()

app.layout = html.Div([
                dcc.RadioItems(id='wheels',
                               options=[{'label':i, 'value':i} for i in df['wheels'].unique()],
                               value=1),
                html.Div(id='wheels-output'),
                html.Hr(),
                dcc.RadioItems(id='colors',options=[{'label':i, 'value':i} for i in df['color'].unique()],
                               value='blue'),
                html.Div(id='colors-output'),
                html.Img(id='display-image',src='children',height=300)
],style={'fontFamily':'Times','fontSize':18})

@app.callback(Output('wheels-output','children'),
              [Input('wheels','value')])


def callback_a(wheels_value):
    return 'You choose {}'.format(wheels_value)

@app.callback(Output('colors-output','children'),
              [Input('colors','value')])


def callback_b(colors_value):
    return 'You choose {}'.format(colors_value)

@app.callback(Output('hover-image', 'src'), [Input('wheels-plot', 'hoverData')])

def callback_image(wheel,color):
    #path = '../data/images/'
    return encode_image(df[(df['wheels'] == wheel) & \
                                  (df['color'] == color)]['image'].values[0])


if __name__ == '__main__':
    app.run_server()
