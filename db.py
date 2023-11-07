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


def add_user_to_database(username, password):
    config = read_config("config.json")

    if config:
        db_config = config.get("db_config")
        if db_config:
            host = db_config.get("host")
            user = db_config.get("user")
            password = db_config.get("password")
            database = db_config.get("database")

            if host and user and password and database:
                connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database
                )
            else:
                print("Incomplete database configuration in config file.")
        else:
            print("Database configuration not found in config file.")
    else:
        print("No config file found.")

    try:
        connection = mysql.connector.connect(
            host='124.70.150.192:3306',
            user='root',
            password='your_password',
            database='your_database'
        )

        cursor = connection.cursor()

        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        data = (username, password)

        cursor.execute(insert_query, data)
        connection.commit()

        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


if __name__ == "__main__":
    username = "user1"  # 你的用户名
    password = "pass1"  # 你的密码

    if add_user_to_database(username, password):
        print(f"User {username} added to the database.")
    else:
        print(f"Failed to add user {username} to the database.")
