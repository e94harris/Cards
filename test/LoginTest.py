import unittest

import pandas as pd

from dataframe.DataFrame import DataFrame
from login.LoginConstructor import LoginConstructor
from login.LoginRequest import LoginRequest
from login.LoginResponse import LoginResponse
from settings.Variables import id_dataframe_value


class MyTestCase(unittest.TestCase):

    def test_encrypt_decrypt(self):
        tmp_string = "Hello World!"
        private_key_path = "private/private_key.pem"
        encrypt_string = DataFrame.encrypt_string(private_key_path, tmp_string)
        res = DataFrame.decrypt_string(private_key_path, encrypt_string)
        self.assertEqual(tmp_string, res)

    def test_encrypt_decrypt_dataframe(self):
        excel_xlsx = "private/login_excel.xlsx"
        private_key_path = "private/private_key.pem"
        crypt_data_frame_path = DataFrame.encrypt_data_frame(excel_xlsx, private_key_path)
        encrypt_data_frame = DataFrame.decrypt_data_frame(crypt_data_frame_path, private_key_path)
        read_excel = pd.read_excel(excel_xlsx)
        self.assertEqual(read_excel[id_dataframe_value][0], encrypt_data_frame[id_dataframe_value][0])
        self.assertNotEqual(read_excel[id_dataframe_value][0], pd.read_excel(crypt_data_frame_path)[id_dataframe_value][0])

    def test_login_wrong_password(self):
        login_request: LoginRequest = LoginRequest("DUPONT", "1234")
        login_constructor: LoginConstructor = LoginConstructor(login_request)
        response: LoginResponse = login_constructor.is_connection_ok()
        self.assertNotEqual("Connexion réussie", response.response)

    def test_login_good_password(self):
        login_request: LoginRequest = LoginRequest("tharris", "123")
        login_constructor: LoginConstructor = LoginConstructor(login_request)
        response: LoginResponse = login_constructor.is_connection_ok()
        self.assertEqual("Connexion réussie", response.response)


if __name__ == '__main__':
    unittest.main()
