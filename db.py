import json

import mysql.connector


def read_config(filename):
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        print(f"Config file {filename} not found.")
        return None


def get_all_users(filename="db_config.json"):
    config = read_config(filename)

    if config:
        db_config = config.get("db_config")
        if db_config:
            host = db_config.get("host")
            user = db_config.get("user")
            pwd = db_config.get("password")
            database = db_config.get("database")

            if host and user and pwd and database:
                try:
                    connection = mysql.connector.connect(
                        host=host,
                        user=user,
                        password=pwd,
                        database=database
                    )

                    cursor = connection.cursor()

                    select_query = "SELECT username, password FROM users"
                    cursor.execute(select_query)
                    users = cursor.fetchall()
                    cursor.close()
                    connection.close()
                    return users
                except Exception as e:
                    print(f"Error: {str(e)}")
                    return []
            else:
                print("Incomplete database configuration in config file.")
        else:
            print("Database configuration not found in config file.")
    else:
        print("No config file found.")


def add_user_to_database(pica_username, pica_pwd, filename="db_config.json"):
    config = read_config(filename)

    if config:
        db_config = config.get("db_config")
        if db_config:
            host = db_config.get("host")
            user = db_config.get("user")
            pwd = db_config.get("password")
            database = db_config.get("database")

            if host and user and pwd and database:
                try:
                    connection = mysql.connector.connect(
                        host=host,
                        user=user,
                        password=pwd,
                        database=database
                    )

                    cursor = connection.cursor()

                    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                    data = (pica_username, pica_pwd)

                    cursor.execute(insert_query, data)
                    connection.commit()

                    cursor.close()
                    connection.close()

                    return True, "Success"
                except Exception as e:
                    return False, str(e)
            else:
                return False, "Incomplete database configuration in config file."
        else:
            return False, "Database configuration not found in config file."
    else:
        return False, "No config file found."


if __name__ == "__main__":
    username = "user1"  # 你的用户名
    password = "pass1"  # 你的密码

    if add_user_to_database(username, password):
        print(f"User {username} added to the database.")
    else:
        print(f"Failed to add user {username} to the database.")
