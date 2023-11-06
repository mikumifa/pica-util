from loginIn import login_request
from punchIn import punch_in

if __name__ == "__main__":
    response = punch_in(session=login_request("xxx", "xxx"))
    print(response.text)
