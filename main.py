from db import get_all_users
from loginIn import login_request
from punchIn import punch_in

if __name__ == "__main__":
    users = get_all_users()  # 获取数据库中的用户账号和密码
    for user in users:
        username = user[0]
        password = user[1]
        if username and password:
            response = punch_in(session=login_request(username, password))
            print(f"Username: {username}, Response: {response.text}")
        else:
            print("Username or password missing in config.")
    else:
        print("No users found in the database.")
else:
    print("No user configurations found in config file.")
