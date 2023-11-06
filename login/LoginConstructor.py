from dataframe.DataFrame import DataFrame
from login.LoginRequest import LoginRequest
from login.LoginResponse import LoginResponse
from settings import Variables
from settings.Variables import id_dataframe_value


class LoginConstructor:

    def __init__(self, request: LoginRequest):
        self.username = request.username
        self.password = request.password

    def is_connection_ok(self):
        res_str = "Échec de la connexion. Veuillez vérifier vos informations d'identification."
        style = {'color': 'red'}
        data_frame = DataFrame.decrypt_data_frame(Variables.student_list_path_crypt, Variables.key_path)
        df = data_frame[data_frame[id_dataframe_value] == self.username]
        if not df.empty:
            df = data_frame[data_frame["MDP"] == self.password]
            if not df.empty:
                res_str = "Connexion réussie"
                style = {'color': 'green'}
        res = LoginResponse(res_str, style)
        return res
