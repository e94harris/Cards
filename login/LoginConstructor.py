import pandas as pd

class loginConstructor:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def process(self):
        df = pd.read_excel('login_excel.xlsx')
        df = df[df['username'] == self.username]
        isDfEmpty = df.empty
        return LoginResponse(isDfEmpty)

