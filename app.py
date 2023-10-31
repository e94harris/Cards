import dash
from dash import html, dcc
from dash.dependencies import Input, Output


# Run Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H2("Page de connexion"),
    html.Div([
        html.Label("Nom d'utilisateur"),
        dcc.Input(id='username_input', type='text', placeholder='Entrez votre nom d\'utilisateur'),
    ]),
    html.Div([
        html.Label("Mot de passe"),
        dcc.Input(id='password-input', type='password', placeholder='Entrez votre mot de passe'),
    ]),
    html.Button("Se connecter", id='login-button', n_clicks=0),
    html.Div(id='login-status'),
])

@app.callback(
    Output('login-status', 'children'),
    [Input('login-button', 'n_clicks')],
    [dash.dependencies.State('username_input', 'value'),
     dash.dependencies.State('password-input', 'value')]
)
def login(n_clicks, username, password):
    if n_clicks > 0:
        if username == 'utilisateur' and password == 'motdepasse':
            return html.Div("Connexion réussie", style={'color': 'green'})
        else:
            return html.Div("Échec de la connexion. Veuillez vérifier vos informations d'identification.", style={'color': 'red'})


if __name__ == '__main__':
    app.run_server(debug=True)