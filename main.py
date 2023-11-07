import json

from loginIn import login_request
from punchIn import punch_in


def read_config(filename):
    try:
        with open(filename, "r") as file:
            config_data = json.load(file)
            return config_data
    except FileNotFoundError:
        print(f"Config file '{filename}' not found.")
        return None


if __name__ == "__main__":
    config = read_config("config.json")
    if config:
        for user_config in config:
            username = user_config.get("username")
            password = user_config.get("password")

            if username and password:
                response = punch_in(session=login_request(username, password))
                print(f"Username: {username}, Response: {response.text}")
            else:
                print("Username or password missing in config.")
    else:
        print("No user configurations found in config file.")
