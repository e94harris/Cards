import sys

key_path = "/etc/secrets/private_key.pem" if sys.platform == "linux" else "private/private_key.pem"
student_list_path_crypt = "data/list_crypt.xlsx"
id_dataframe_value = "ID"
name_dataframe_value = "Nom"
password_dataframe_value = "MDP"