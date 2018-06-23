import dash
# import dash_auth
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
import plotly
import plotly.offline as pyo
import plotly.graph_objs as go
from scipy import stats
import numpy as np

#USERNAME_PASSWORD_PAIRS = [
#    ['elanding', '123']
#]

app = dash.Dash(__name__)

# auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)
server = app.server


# app.scripts.config.serve_locally = True



markdown_text = '''
Adjust the values of alpha and beta. Here beta is the scale value.
'''

app.layout = html.Div([
    html.H4('Gamma Distribution'),
    dcc.Markdown([markdown_text]),
    html.Div([

    html.Div([
    html.Label('Enter the value of alpha'),
    dcc.Slider(
            id='slider-alpha',
            min=0.5,
            max=10.0,
            step=0.5,
            value=3,
            marks={i:i for i in range(11)}
        )], style={'width':'48%', 'display': 'inline-block', 'marginRight': 20}),

    html.Div([
    html.Label('Enter the value of beta'),
    dcc.Slider(
            id='slider-beta',
            min=0.5,
            max=3,
            step=0.25,
            value=0.5,
            marks={0.5:0.5, 1: 1.0, 1.5:1.5, 2:2, 2.5:2.5, 3:3}
        )], style={'width':'48%', 'display': 'inline-block', 'marginLeft': 20}),

        ], style={'marginBottom': 50}),

html.Div([dcc.Graph(id='gamma-plot', animate=True, style={'height':500})])

], style={'padding':10})

@app.callback(
    Output('gamma-plot', 'figure'),
    [Input('slider-alpha', 'value'),
     Input('slider-beta', 'value')])
def plot(alpha, beta):
    x = np.linspace(0, 20, 1000)
    y = stats.gamma.pdf(x, a=alpha, scale=beta)
    data = [go.Scatter(x=x,y=y, mode='lines')]

    layout = go.Layout(
    xaxis=dict(title="x", range=[0, 20], autorange=True),
    yaxis=dict(title="density",range=[0, 0.5], autorange=True),
    title="Gamma Distribution"
    )

    fig = go.Figure(data = data, layout=layout)
    return fig






# Alternative way to graph:
    # return {
    #     'data': [{
    #         'x': dff['X'],
    #         'y': dff['Probability'],
    #         'type': 'bar'
    #     }],
    #     'layout': {
    #         'margin' : 10,
    #         'title' : 'Probability Distribution'
    #     }
    # }



app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)
