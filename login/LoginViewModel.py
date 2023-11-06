from dash import html

from login.LoginResponse import LoginResponse


class LoginViewModel:

    def __init__(self, response: LoginResponse):
        self.response = response

    def generate_view(self):
        return html.Div(self.response.response, style=self.response.style)
