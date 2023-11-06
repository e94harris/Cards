import pandas as pd
from cryptography.fernet import Fernet
import settings.Variables


class DataFrame:

    @staticmethod
    def apply_cryptography_to_data_frame(excel_file_path, key_path, crypto_fct):
        df = pd.read_excel(excel_file_path)
        columns = df.columns
        structured_array = df.to_records(index=False)
        list_of_strings = []
        for d in structured_array:
            for elm in d:
                list_of_strings.append(str(elm))
        non_crypt_list = [crypto_fct(key_path, elm) for elm in list_of_strings]
        res = []
        for i in range(0, len(non_crypt_list), 4):
            res.append([non_crypt_list[i], non_crypt_list[i + 1], non_crypt_list[i + 2], non_crypt_list[i + 3]])
        df = pd.DataFrame(res, columns=columns)
        return df

    @staticmethod
    def encrypt_string(key_path, string):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        f = Fernet(key)
        return f.encrypt(string.encode()).decode()

    @staticmethod
    def decrypt_string(key_path, string):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        f = Fernet(key)
        return f.decrypt(string).decode()

    @staticmethod
    def encrypt_data_frame(excel_file_path, key_path):
        df = DataFrame.apply_cryptography_to_data_frame(excel_file_path, key_path, DataFrame.encrypt_string)
        df.to_excel(settings.Variables.student_list_path_crypt, index=False)
        return settings.Variables.student_list_path_crypt

    @staticmethod
    def decrypt_data_frame(excel_file_path, key_path):
        return DataFrame.apply_cryptography_to_data_frame(excel_file_path, key_path, DataFrame.decrypt_string)
