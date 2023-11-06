from loginIn import login_request
from punchIn import punch_in

if __name__ == "__main__":
    response = punch_in(session=login_request("mikumifa", "ldxy041015"))
    print(response.text)
