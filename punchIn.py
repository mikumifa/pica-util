from loginIn import login_request


def punch_in(session=None):
    baseUrl = "https://api.manhuapica.com/"
    url = "users/punch-in"

    response = session.post(baseUrl + url)
    return response



