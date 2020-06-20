import dash
import dash_core_components as doc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children = [html.H1('Hello Dash!'),\
                                  html.Div('Dash: Web Dashboards with Python')])

if __name__ == '__main__':
  app.run_server(debug=True)
